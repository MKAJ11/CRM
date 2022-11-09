# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Lead(models.Model):
    _inherit = "crm.lead"

    estimate_line_custom_ids = fields.One2many(
        'crm.estimate.line.custom',
        'crmlead_custom_id',
        string='Estimate Lines',
        copy=False,
    )

    def action_crm_sale_estimate_custom(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('odoo_sale_estimates.action_estimate')
        action['domain'] = [('crm_custom_id','=', self.id)]
        return action
