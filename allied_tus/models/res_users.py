# -*- coding: utf-8 -*-
"""
    Res User and added new field
"""
from odoo import api, fields, models


class ResUsers(models.Model):
    """
        Inherits res user and added some new filed
    """
    _inherit = "res.partner"

    is_distributor = fields.Boolean(string="Is Distributor")
    is_contractor = fields.Boolean(string="Is Contractor")
    is_installers = fields.Boolean(string="Is Installers")
    sheet_price = fields.Float(string="Sheet SQ FT Price",  required=False, )
