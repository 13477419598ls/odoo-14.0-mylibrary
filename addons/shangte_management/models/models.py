# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shangte_management(models.Model):
    _name = 'shangte_management.shangte_management'
    _description = 'shangte_management.shangte_management'

    CRM_frame_code = fields.Char('CRM框架编码')
    CRM_business_code = fields.Char('CRM商机编码')
    HIC_business_code = fields.Char('CRM商机编码')
    value = fields.Integer()


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
