# -*- coding: utf-8 -*-
"""
    Stock Picking
"""
from odoo import api, fields, models


class StockPicking(models.Model):
    """
        Inherits Stock Picking
    """
    _inherit = "stock.picking"

    @api.model
    def create(self, vals):
        if vals.get('origin'):
            order_id = self.env['sale.order'].search([('name', '=', vals.get('origin'))])
            if order_id:
                estimate_id = self.env['sale.estimate'].search([('quotation_id', '=', order_id.id)])
                if estimate_id and estimate_id.crm_custom_id and estimate_id.crm_custom_id.location_id:
                    vals.update({'location_dest_id': estimate_id.crm_custom_id.location_id.id})
        res = super(StockPicking, self).create(vals)
        return res
