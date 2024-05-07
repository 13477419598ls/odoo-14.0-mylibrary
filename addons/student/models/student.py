# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _inherit = 'student.student'

    math = fields.Float('数学成绩')


