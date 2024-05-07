# -*- coding: utf-8 -*-
# from odoo import http


# class ShangteManagement(http.Controller):
#     @http.route('/shangte_management/shangte_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shangte_management/shangte_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shangte_management.listing', {
#             'root': '/shangte_management/shangte_management',
#             'objects': http.request.env['shangte_management.shangte_management'].search([]),
#         })

#     @http.route('/shangte_management/shangte_management/objects/<model("shangte_management.shangte_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shangte_management.object', {
#             'object': obj
#         })
