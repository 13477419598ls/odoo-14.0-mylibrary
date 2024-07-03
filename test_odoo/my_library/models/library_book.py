from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = '图书馆描述'
    _order = 'date_release desc, name'  # 按发行日期降序排序，如果日期相同则按书名升序排序
    _rec_name = 'short_name'

    name = fields.Char('书名', required=True)
    short_name = fields.Char('短标题', required=True)
    date_release = fields.Date('发行日期')
    author_ids = fields.Many2many(
        'res.partner',
        string='作者')

    notes = fields.Text('内部说明')
    state = fields.Selection(
        [('draft', '不可用'),
         ('available', '可用'),
         ('lost', '丢失')],
        '状态', default="draft")
    description = fields.Html('描述')
    cover = fields.Binary('图书封面')
    out_of_print = fields.Boolean('是否绝版')
    date_updated = fields.Datetime('最后更新')
    pages = fields.Integer('页数')
    reader_rating = fields.Float(
        '读者平均评分',
        digits=(14, 4),  # 可选精度（总计, 小数）
    )
    cost_price = fields.Float('书本成本', digits='Book Price')

    # 1.添加所要使用的字段来存储币种
    currency_id = fields.Many2one(
        'res.currency', string='货币')
    # 2.添加货币字段来存储金额
    retail_price = fields.Monetary(
        '零售价',
        # currency_field='currency_id',  # 如果以currency_id名称的字段存储币种信息,可以在货币字段中省略掉currency_field属性。
    )

    # 向图书模型添加图书出版商的many-to-one字段
    publisher_id = fields.Many2one(
        'res.partner',
        string='出版商',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
    )
    # 为出版社城市添加一个关联字段
    publisher_city = fields.Char(
        '出版商城市',
        related='publisher_id.city',
        readonly=True)

    # 添加一个many-to-one字段来关联图书类别
    # category_id = fields.Many2one('library.book.category', '类别')

    age_days = fields.Float(
        string='发布天数',
        compute='_compute_age',
        inverse='_inverse_age',
        search='_search_age',
        store=False,        # optional
        compute_sudo=False  # optional
    )

    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='参考文件')

    # 添加模型属性来创建数据库约束
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', '书名必须是唯一的。'),
        ('positive_page', 'CHECK(pages>0)', '页数必须为正数')
    ]

    # 添加一个模型方法来创建Python代码约束：
    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError('发布日期必须是过去')

    # 添加计算逻辑的方法
    @api.depends('date_release')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0

    # 添加方法及实现写入计算字段的逻辑
    def _inverse_age(self):
        today = fields.Date.today()
        for book in self.filtered('date_release'):
            d = today - timedelta(days=book.age_days)
            book.date_release = d

    # 实现允许在计算字段中进行搜索的逻辑
    def _search_age(self, operator, value):
        today = fields.Date.today()
        value_days = timedelta(days=value)
        value_date = today - value_days
        # 运算符转换：
        # age_days > value -> date < value_date
        operator_map = {
            '>': '<', '>=': '<=',
            '<': '>', '<=': '>=',
        }
        new_op = operator_map.get(operator, operator)
        return [('date_release', new_op, value_date)]

    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    @api.model
    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')

    # 获取其它模型的空记录集
    def log_all_library_members(self):
        library_member_model = self.env['library.member']  # 这是library.member的空记录集
        all_members = library_member_model.search([])
        print('ALL MEMBERS:', all_members)
        return True


# 为出版社的书籍添加one-to-many字段
class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'
    published_book_ids = fields.One2many(
        'library.book', 'publisher_id',
        string='出版商的书籍')

    authored_book_ids = fields.Many2many(
        'library.book',
        string='著作',
        # relation='library_book_res_partner_rel' # optional

        count_books=fields.Integer(
        '著作数量',
        compute='_compute_count_books')
    )

    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)


class LibraryMember(models.Model):
    _inherit = 'res.partner'
    _name = 'library.member'
