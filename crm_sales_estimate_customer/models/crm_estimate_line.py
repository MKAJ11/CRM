# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmEstimateLine(models.Model):
    _name = 'crm.estimate.line.custom'
    _description = 'CRM Estimate Line'

    crmlead_custom_id = fields.Many2one(
        'crm.lead',
        string='CRM', 
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )
    product_uom_qty = fields.Float(
        string='Quantity', 
        digits='Product Unit of Measure',
        required=True, 
        default=1.0
    )
    product_uom = fields.Many2one(
        'uom.uom',
        string='Unit of Measure', 
        required=True
    )
    price_unit = fields.Float(
        'Unit Price', 
        required=True, 
        digits='Product Price',
        default=0.0
    )
    product_description = fields.Char(
        string='Description'
    )
    company_id = fields.Many2one(
        related='crmlead_custom_id.company_id', 
        string='Company', 
        store=False, 
        readonly=True
    )
    is_estimate_created = fields.Boolean(
        string='Is Estimate Created ?',
        readonly=True,
        copy=False,
    )
    estimate_custom_id = fields.Many2one(
        'sale.estimate',
        string='Sales Estimate',
        copy=False,
        readonly=True,
    )
    estimate_line_custom_id = fields.Many2one(
        'sale.estimate.line',
        string='Sales Estimate Line',
        copy=False,
        readonly=True,
    )

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.product_uom_qty * rec.price_unit

    total_price = fields.Float(string="Total Price",  required=False, compute="_compute_total_price")

    @api.onchange('product_id')
    def product_id_change(self):
        if self.product_id:
            self.product_uom_qty = 1.0
            self.product_uom = self.product_id.uom_id.id
            self.price_unit = self.product_id.list_price
            self.product_description = self.product_id.display_name
           

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: