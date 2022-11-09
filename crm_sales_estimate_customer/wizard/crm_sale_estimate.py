# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CrmsaleEstimateWizard(models.Model):
    _name = 'crmsale.estimate.wizard.cust'
    _description = 'CRM Sale Estimate Wizard'
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
    )

    def prepare_sales_estimate_vals_custom(self, crm_id):
        return {
            'partner_id': self.partner_id.id,
            'pricelist_id': self.partner_id.property_product_pricelist.id,
            'payment_term_id': self.partner_id.property_payment_term_id.id,
            'team_id': crm_id.team_id.id,
            'crm_custom_id': crm_id.id
        }

    def prepare_sale_estimate_line_vals_custom(self, line, sale_estimate):
        return {
            'product_id': line.product_id.id,
            'product_uom_qty': line.product_uom_qty,
            'product_uom': line.product_uom.id,
            'price_unit': line.price_unit,
            'product_description': line.product_description,
            'estimate_id': sale_estimate.id
        }

    def create_sale_estimate_custom(self):
        self.ensure_one()
        sale_estimate_obj = self.env['sale.estimate']
        sale_estimate_line_obj = self.env['sale.estimate.line']
        crm_id = self.env['crm.lead'].browse(self._context.get('crm_id'))
        sale_estimate_list = []
        if not crm_id.estimate_line_custom_ids:
            raise UserError(_('No estimate lines are found.'))
            
        # if all(line.is_estimate_created for line in crm_id.estimate_line_custom_ids):
        #     raise UserError(_('All estimate lines are created.'))

        estimate_vals = self.prepare_sales_estimate_vals_custom(crm_id)
        sale_estimate = sale_estimate_obj.create(estimate_vals)

        sale_estimate_list.append(sale_estimate.id)
        
        for line in crm_id.estimate_line_custom_ids:  
            # if line.is_estimate_created != True:
            estimate_line_vals = self.prepare_sale_estimate_line_vals_custom(line,sale_estimate)
            sale_estimate_line = sale_estimate_line_obj.create(estimate_line_vals)
            line.is_estimate_created = True
            line.estimate_line_custom_id = sale_estimate_line.id
            line.estimate_custom_id = sale_estimate.id
