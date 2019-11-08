# -*- coding: utf-8 -*-
from odoo import http

# class Educenter(http.Controller):
#     @http.route('/educenter/educenter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/educenter/educenter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('educenter.listing', {
#             'root': '/educenter/educenter',
#             'objects': http.request.env['educenter.educenter'].search([]),
#         })

#     @http.route('/educenter/educenter/objects/<model("educenter.educenter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('educenter.object', {
#             'object': obj
#         })