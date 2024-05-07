# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'student.student'
    _description = 'student.student'

    name = fields.Char("姓名")
    score = fields.Float("成绩")
    num = fields.Integer("学号")


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
