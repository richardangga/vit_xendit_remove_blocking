# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.vit_xendit_callback.controllers.controllers import VitXenditCallback
import simplejson
import time
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class VitXenditCallback2(VitXenditCallback):
	@http.route('/xendit/invoice/paid', methods=['GET','POST'], auth='public', type='json')
	def invoice_paid(self, **kw):
		# return "Hello, world"
		res = super(VitXenditCallback2, self).invoice_paid(kw)
		sale_order = request.env['sale.order'].sudo().search([('name','=',data['external_id'])])
		sale_order.action_remove_delivery_block()
		return res

	@http.route('/xendit/fva/paid', methods=['GET','POST'], auth='public', type='json')
	def fva_paid(self, **kw):
		
		tes = super(VitXenditCallback2, self).fva_paid(kw)
		res_partner = request.env['res.partner'].sudo().search([('va_number','=',data['account_number'])])
		res_partner.action_remove_delivery_block()
		return tes