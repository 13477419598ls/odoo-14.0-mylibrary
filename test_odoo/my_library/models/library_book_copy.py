from odoo import models, fields, api

class LibraryBookCopy(models.Model):
    _name = 'library.book.copy'
    _inherit = 'library.book'
    _description = "图书馆书籍的副本"
