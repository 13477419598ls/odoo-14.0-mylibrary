# -*- coding: utf-8 -*-
# from odoo import http


# class ItsmSystemMaintenanceInformation(http.Controller):
#     @http.route('/xc_itsm/xc_itsm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xc_itsm/xc_itsm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xc_itsm.listing', {
#             'root': '/xc_itsm/xc_itsm',
#             'objects': http.request.env['xc_itsm.xc_itsm'].search([]),
#         })

#     @http.route('/xc_itsm/xc_itsm/objects/<model("xc_itsm.xc_itsm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xc_itsm.object', {
#             'object': obj
#         })
