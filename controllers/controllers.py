# -*- coding: utf-8 -*-
from odoo import http

# class TrainCarRequest(http.Controller):
#     @http.route('/train_car_request/train_car_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/train_car_request/train_car_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('train_car_request.listing', {
#             'root': '/train_car_request/train_car_request',
#             'objects': http.request.env['train_car_request.train_car_request'].search([]),
#         })

#     @http.route('/train_car_request/train_car_request/objects/<model("train_car_request.train_car_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('train_car_request.object', {
#             'object': obj
#         })