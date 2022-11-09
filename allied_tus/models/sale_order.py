# -*- coding: utf-8 -*-
"""
    Sale Order
"""
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
        Inherits Sale order
    """
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        if vals.get('origin'):
            estimate_order_id = self.env['sale.estimate'].search([('number', '=', vals.get('origin'))])
            if estimate_order_id and estimate_order_id.crm_custom_id and estimate_order_id.crm_custom_id.partner_shipping_id:
                vals.update({'partner_shipping_id': estimate_order_id.crm_custom_id.partner_shipping_id.id})
        res = super(SaleOrder, self).create(vals)
        return res
