# -*- coding: utf-8 -*-
from odoo import http
import json

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
class InfoTimetable(http.Controller):
    @http.route('/ajax/search_schedule', auth='public', type='json', csrf=False, methods=['POST', 'OPTIONS'], cors='*')
    def AjaxSearchSchedule(self, query=''):
        if http.request.httprequest.method == 'OPTIONS':
            return json.dump([''])
# @http.route('/ajax/search_schedule', auth='public', type='json', methods=['POST'])
#     def AjaxSearchSchedule(self, query=''):
        objects = http.request.env['educenter.courses'].sudo().search([
            ('name', 'ilike', query)
        ], limit=10, order="name asc")
        return json.dumps(
            [{'id': obj.id, 'price': obj.name} for obj in objects]
        )