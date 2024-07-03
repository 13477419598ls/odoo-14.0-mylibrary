from odoo import models, fields, api


class BookCategory(models.Model):
    _name = 'library.book.category'
    _parent_store = True
    _parent_name = "parent_id"  # 如果字段为“parent_id”，则可选
    parent_path = fields.Char(index=True)

    name = fields.Char('类别')
    parent_id = fields.Many2one(
        'library.book.category',
        string='父类别',
        ondelete='restrict',
        index=True)
    child_ids = fields.One2many(
        'library.book.category',
        'parent_id',
        string='子类别')


# 新增一个防止循环关联的检查
@api.constrains('parent_id')
def _check_hierarchy(self):
    if not self._check_recursion():
        raise models.ValidationError('错误！不能创建递归类别。')
