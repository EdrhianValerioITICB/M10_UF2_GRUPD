# -*- coding: utf-8 -*-
# from odoo import http


# class Facturacion(http.Controller):
#     @http.route('/facturacion/facturacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facturacion/facturacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('facturacion.listing', {
#             'root': '/facturacion/facturacion',
#             'objects': http.request.env['facturacion.facturacion'].search([]),
#         })

#     @http.route('/facturacion/facturacion/objects/<model("facturacion.facturacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facturacion.object', {
#             'object': obj
#         })
