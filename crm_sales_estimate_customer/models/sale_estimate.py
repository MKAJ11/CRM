# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleEstimate(models.Model):
    _inherit = "sale.estimate"

    crm_custom_id = fields.Many2one(
        'crm.lead',
        string='CRM Pipeline/Opportunity',
        copy=False,
    )
