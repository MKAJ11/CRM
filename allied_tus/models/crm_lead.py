# -*- coding: utf-8 -*-
"""
    Res Partner and added new field
"""
import math
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


def ceil(x, s):
    return s * math.ceil(float(x) / s)


class CrmLead(models.Model):
    """
        Inherits res partner and added some new filed
    """
    _inherit = "crm.lead"

    process_id = fields.Many2one(comodel_name="allied.process", string="Process", required=False, tracking=True)
    subx_region_id = fields.Many2one(comodel_name="subx.region", string="Region", required=False, tracking=True)
    subx_po = fields.Char(string="SBUX PO", required=False, )
    is_subx = fields.Boolean(string="Is subx", compute="_get_is_subx")
    distributor_id = fields.Many2one(comodel_name="res.partner", string="Distributor", required=False, tracking=True)
    general_contractor_id = fields.Many2one(comodel_name="res.partner", string="General Contractor", required=False, tracking=True)
    installer_id = fields.Many2one(comodel_name="res.partner", string="Installer", required=False, )
    store = fields.Char(string="Store #", required=False, )
    cpn = fields.Char(string="CPN #", required=False, )
    scope_id = fields.Many2one(comodel_name="allied.scope", string="Scope", required=False, )
    installation_date = fields.Date(string="Installation Date", required=False, )
    job_days = fields.Char(string="# Days ", required=False, )
    procurement_id = fields.Many2one(comodel_name="procurement.data", string="Procurement", required=False, tracking=True)
    quoted_date = fields.Date(string="Quoted Date", required=False)
    is_flanges_pallet = fields.Boolean(string="Flanges on Pallet?")
    delivery_contact_info = fields.Char(string="Delivery Contact Info", required=False, )
    is_materials_wo = fields.Boolean(string="Materials WO")
    is_flanges_wo = fields.Boolean(string="Flanges WO")
    is_bol = fields.Boolean(string="BOL to Allied")
    freight_tracking_info = fields.Char(string="Freight Tracking Info")
    flanges_tracking_info = fields.Char(string="Flanges Tracking Info")
    gc_po = fields.Char(string="GC PO")
    is_quick_books = fields.Boolean(string="Quick Books")
    is_credit_file = fields.Boolean(string="Credit App on File")
    is_signed_estimate = fields.Boolean(string="Signed Estimate or PO")
    contractor_line_ids = fields.One2many(comodel_name="contractor.line", inverse_name="crm_lead_id",
                                          string="Contractor", required=False, tracking=True)
    deadline = fields.Date(string="Deadline", required=False)
    leader_id = fields.Many2one(comodel_name="res.partner", string="Leader", required=False, )

    opp_street = fields.Char(string="Street", required=False, )
    opp_street2 = fields.Char(string="Street", required=False, )
    opp_city = fields.Char(string="Opp City", required=False, )
    opp_state_id = fields.Many2one(comodel_name="res.country.state", string="Opp State", required=False, )
    opp_country_id = fields.Many2one(comodel_name="res.country", string="Opp Country", required=False, )
    material_sqft = fields.Char(string="Material SQFT", required=False, )
    color = fields.Char(string="Color", required=False, )
    co_reason = fields.Char(string="CO Reason", required=False, )
    qc_concerns = fields.Char(string="QC Concerns", required=False, )
    shipping_deadline = fields.Date(string="Deadline", required=False, )
    shipping_delivery = fields.Date(string="Delivery Date", required=False, )
    store_number = fields.Char(string="Store #", required=False, )
    site_general_contractor_id = fields.Many2one(comodel_name="res.partner", string="General Contractor",
                                                 required=False, )
    site_installer_id = fields.Many2one(comodel_name="res.partner", string="Installer", required=False, )
    site_opp_street = fields.Char(string="Street", required=False, )
    site_opp_street2 = fields.Char(string="Street", required=False, )
    site_opp_city = fields.Char(string="Opp City", required=False, )
    site_opp_state_id = fields.Many2one(comodel_name="res.country.state", string="Opp State", required=False, )
    site_opp_country_id = fields.Many2one(comodel_name="res.country", string="Opp Country", required=False, )
    freight_address = fields.Char(string="Freight Address", required=False, )
    fedex_price = fields.Float(string="FedEx Price", required=False, )
    partner_shipping_id = fields.Many2one(
        'res.partner',
        string='Delivery Address',
        domain="[('type', '=', 'delivery')]",
        help="Delivery address for shipping." )
    actual_ship_date = fields.Date(string="Actual Ship Date", required=False, )
    tracking_info = fields.Char(string="Tracking Info", required=False, )
    ship_name = fields.Char(string="Name", required=False, )
    ship_email = fields.Char(string="Email", required=False, )
    ship_phone = fields.Char(string="Phone", required=False, )
    shipping_broker = fields.Char(string="Shipping Broker", required=False, )
    truck_line = fields.Char(string="Truck Line", required=False, )
    shipping_cost = fields.Float(string="Shipping Cost", required=False, )

    general_contractor_other_id = fields.Many2one(comodel_name="res.partner", string="General Contractor",
                                                  required=False, )
    company_other_id = fields.Many2one(comodel_name="res.company", string="Company", required=False, )
    contact_other_id = fields.Many2one(comodel_name="res.partner", string="Contact", required=False, )
    po_number = fields.Char(string="Purchase Number", required=False, )
    req_delivery_date = fields.Date(string="Requested delivery Date", required=False, )
    req_ship_date = fields.Date(string="Requested Ship Date", required=False, )
    project_contact_id = fields.Many2one(comodel_name="res.partner", string="General Contractor", required=False, tracking=True)
    declared_sqft_number = fields.Char(string="Declared SQ FT", required=False, tracking=True)

    estimator_color = fields.Selection(string="Color", selection=[('pewter', 'Pewter')], required=False,
                                       default='pewter')
    project_type = fields.Selection(string="Project Type",
                                    selection=[('new', 'New'), ('remodel', 'Remodel'), ('retrofit', 'Retrofit'),
                                               ('repair', 'Repair')],
                                    required=False, tracking=True)
    liner_ft = fields.Float(string="Liner FT", required=False, )
    base_height = fields.Float(string="Base Height", required=False, )
    sqft = fields.Float(string="SQ FT", required=False, )
    floor_sinks = fields.Float(string="Floor Sinks", required=False, )
    floor_drains = fields.Float(string="Floor Drains/CO", required=False, )
    trench_drains = fields.Float(string="Trench Drains/ Grease Traps", required=False, )
    sheet_product_id = fields.Many2one(comodel_name="product.product", string="Sheet Product", required=False, )
    speed_flex_product_id = fields.Many2one(comodel_name="product.product", string="Speed Flex Product",
                                            required=False, )
    base_cape_product_id = fields.Many2one(comodel_name="product.product", string="Base Cape Product", required=False, )
    epoxy_product_id = fields.Many2one(comodel_name="product.product", string="Epoxy Product", required=False, )
    seam_tape_product_id = fields.Many2one(comodel_name="product.product", string="Seam Tape Product", required=False, )
    speed_flex_mixer_product_id = fields.Many2one(comodel_name="product.product", string="Speed Flex Mixer",
                                                  required=False, )
    base_screws_product_id = fields.Many2one(comodel_name="product.product", string="Base Screws Product",
                                             required=False, )
    floor_sinks_product_id = fields.Many2one(comodel_name="product.product", string="Floor Sinks Product",
                                             required=False, )
    floor_drains_product_id = fields.Many2one(comodel_name="product.product", string="Floor Drains Product",
                                              required=False, )
    floor_trench_product_id = fields.Many2one(comodel_name="product.product", string="Trench / Grease Trap Product")
    number_10_screw_product_id = fields.Many2one(comodel_name="product.product", string="10# Screw Product")
    e_1600_product_id = fields.Many2one(comodel_name="product.product", string="E6100, case of 12 Product")
    sqft_product_id = fields.Many2one(comodel_name="product.product", string="SQ FT INCL BASE Product")
    location_id = fields.Many2one(comodel_name="stock.location", string="Ship To Location")

    @api.onchange('estimate_line_custom_ids', 'sqft', 'liner_ft', 'partner_id')
    def count_material_price(self):
        if self.partner_id:
            self.contact_name = self.partner_id.name
        self.material_price = 0
        if self.estimate_line_custom_ids:
            total_unit_price = sum(self.estimate_line_custom_ids.mapped('total_price'))
            temp_sum = self.sqft + self.liner_ft
            if temp_sum:
                self.material_price = total_unit_price / (self.sqft + self.liner_ft)
            else:
                self.material_price = 0
        else:
            if self.partner_id:
                self.material_price = self.partner_id.sheet_price

    def generate_estimate_line(self, product_id=False, qty=False):
        line_val = (0, 0, {
            'product_id': product_id.id,
            'product_description': product_id.name,
            'product_uom_qty': qty,
            'product_uom': product_id.uom_id.id,
            'price_unit': product_id.lst_price,
        })
        return line_val

    def create_estimate_line(self):
        self.estimate_line_custom_ids.unlink()
        order_line_list = []
        product_obj = self.env['product.product']
        product_id = self.sheet_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.sheets)
            order_line_list.append(line_val)
        product_id = self.epoxy_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.epoxy)
            order_line_list.append(line_val)
        product_id = self.speed_flex_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.speed_flex)
            order_line_list.append(line_val)
        product_id = self.seam_tape_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.seam_tape)
            order_line_list.append(line_val)
        product_id = self.speed_flex_mixer_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.speed_flex_static)
            order_line_list.append(line_val)
        product_id = self.base_cape_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.base_screws)
            order_line_list.append(line_val)
        product_id = self.floor_sinks_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.floor_sink_flang)
            order_line_list.append(line_val)
        product_id = self.floor_drains_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.floor_drain)
            order_line_list.append(line_val)
        product_id = self.floor_trench_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.floor_trench)
            order_line_list.append(line_val)
        product_id = self.number_10_screw_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.number_10_screws)
            order_line_list.append(line_val)
        product_id = self.e_1600_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.e6100_tube)
            order_line_list.append(line_val)
        product_id = self.sqft_product_id
        if product_id:
            line_val = self.generate_estimate_line(product_id, qty=self.sqft_incl_base)
            order_line_list.append(line_val)
        self.estimate_line_custom_ids = order_line_list
        self.count_material_price()

    @api.depends('project_type', 'liner_ft', 'base_height', 'sqft', 'fedex_parcel', 'material_price',
                 'floor_drains', 'extra_sheets', 'floor_sinks', 'floor_trench', 'base_trim',
                 'threshold')
    def _compute_material(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        for rec in self:
            rec.base_trim = rec.sheets = rec.epoxy = rec.speed_flex = rec.seam_tape = rec.speed_flex_static = rec.base_screws = rec.floor_sink_flang = rec.floor_drain = rec.floor_trench = rec.number_10_screws = rec.e6100_tube = rec.sqft_incl_base = rec.total_material_price = 0
            if rec.sqft:
                sheet_cal = math.ceil((((rec.sqft + (rec.liner_ft * rec.base_height)) * 1.1) / 40) + 2)
                rec.sheets = sheet_cal
                if rec.project_type == "repair":
                    rec.epoxy = (math.ceil((rec.sheets + rec.extra_sheets) / 1.75)) + 1
                if rec.project_type == "new":
                    rec.epoxy = (math.ceil((rec.sheets + rec.extra_sheets) / 2)) + 1
                if rec.project_type == "retrofit":
                    rec.epoxy = (math.ceil((rec.sheets + rec.extra_sheets) / 1.5)) + 3
                if rec.project_type == "remodel":
                    rec.epoxy = (math.ceil((rec.sheets + rec.extra_sheets) / 1.5))

                s_f_cal = math.ceil((((rec.sheets + rec.extra_sheets) * 13) / 50) + (0.33 * (
                        rec.floor_sinks + rec.floor_drains + rec.trench_drains)) + 1)
                rec.speed_flex = s_f_cal

                seam_tape = math.ceil(((((rec.sheets + rec.extra_sheets) * 13) / 180) * 2) + 2)
                rec.seam_tape = seam_tape

                rec.speed_flex_static = rec.seam_tape
                rec.base_screws = (ceil((rec.liner_ft / 8) * 13, 500)) / 500
                rec.floor_sink_flang = rec.floor_sinks
                rec.floor_drain = rec.floor_drains
                rec.floor_trench = rec.trench_drains

                number_10_screws = (((rec.threshold) * 2) + (
                        (rec.floor_drain * 5) + (rec.floor_sink_flang * 12) + (rec.floor_trench * 50)))
                rec.number_10_screws = ceil(number_10_screws, 25) / 25
                e_tube = ceil(((rec.liner_ft + rec.threshold + rec.floor_sink_flang + rec.floor_trench) / 30), 12) / 12
                rec.e6100_tube = e_tube
                rec.sqft_incl_base = (rec.sheets + rec.extra_sheets) * 40
                rec.total_material_price = (rec.material_price * rec.sqft_incl_base) + rec.fedex_parcel
                rec.base_trim = math.ceil((rec.liner_ft + 32) / 8)

    sheets = fields.Float(string="Sheets", required=False, compute="_compute_material")
    extra_sheets = fields.Float(string="Extra Sheets", required=False)
    epoxy = fields.Float(string="Epoxy", required=False, compute="_compute_material")
    speed_flex = fields.Float(string="SpeedFlex Cartridge", required=False, compute="_compute_material")
    seam_tape = fields.Float(string="Seam Tape", required=False, compute="_compute_material")
    speed_flex_static = fields.Float(string="SpeedFlex Static Mixer Tip", required=False, compute="_compute_material")
    base_trim = fields.Float(string="Base Trim", required=False, compute="_compute_material")
    base_screws = fields.Float(string="Base Screws, box of 500", required=False, compute="_compute_material")
    threshold = fields.Float(string="Threshold", required=False)
    floor_sink_flang = fields.Float(string="Floor Sinks Flanges", required=False, compute="_compute_material")
    floor_drain = fields.Float(string="Floor Drain / Clean Out Flanges", required=False, compute="_compute_material")
    floor_trench = fields.Float(string="Trench / Grease Trap Flanges", required=False, compute="_compute_material")
    number_10_screws = fields.Float(string="#10 Screws/anchors, 25 sets per bag", required=False,
                                    compute="_compute_material")
    currency_id = fields.Many2one('res.currency', readonly=True, default=lambda x: x.env.company.currency_id)
    e6100_tube = fields.Float(string="E6100, case of 12 tubes", required=False, compute="_compute_material")
    sqft_incl_base = fields.Float(string="SQ FT INCL BASE", required=False, compute="_compute_material")
    material_price = fields.Float(string="Material SQ FT Price", required=False, default=1)
    fedex_parcel = fields.Float(string="FedEx parcel freight for drain flanges", required=False, )
    total_material_price = fields.Float(string="Total Material Price", required=False, compute="_compute_material")

    @api.depends('process_id')
    def _get_is_subx(self):
        for rec in self:
            if rec.process_id.name == "SBUX":
                rec.is_subx = True
            else:
                rec.is_subx = False

    def create_estimate_quotation(self):
        if not self.contractor_line_ids.contractor_id:
            raise UserError(_("You can not set Bidding Contractor!!"))
        for contractor_id in self.contractor_line_ids:
            wizard_id = self.env['crmsale.estimate.wizard.cust'].with_context(crm_id=self.id).create(
                {'partner_id': contractor_id.contractor_id.id})
            wizard_id.create_sale_estimate_custom()

        action = {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.estimate',
            'name': "Sale Estimate",
            'view_mode': 'tree',
        }
        return action


class ContractorLine(models.Model):
    _name = 'contractor.line'
    _description = 'Contractor Line'

    crm_lead_id = fields.Many2one(comodel_name="crm.lead", string="Contractor", required=False, )
    company_id = fields.Many2one(comodel_name="res.company", string="Company", related="crm_lead_id.company_id")
    contractor_id = fields.Many2one(comodel_name="res.partner", string="Name", required=False,
                                    domain="[('is_contractor', '=', True)]")
    phone = fields.Char(string="Phone", required=False, )
    email = fields.Char(string="Email", required=False, )
    is_notified = fields.Boolean(string="Submitted")
    due_date = fields.Date(string="Due Date", required=False, )

    @api.onchange('contractor_id')
    def _onchange_contractor_id(self):
        for rec in self:
            rec.email = rec.contractor_id.email
            rec.phone = rec.contractor_id.phone


class AlliedProcess(models.Model):
    _name = 'allied.process'
    _rec_name = 'name'
    _description = 'Allied Process'

    name = fields.Char("Process")


class SubxRegion(models.Model):
    _name = 'subx.region'
    _rec_name = 'name'
    _description = 'Subx Region'

    name = fields.Char("SUBX Region")


class AlliedType(models.Model):
    _name = 'allied.type'
    _rec_name = 'name'
    _description = 'Type'

    name = fields.Char("Type")


class AlliedScope(models.Model):
    _name = 'allied.scope'
    _rec_name = 'name'
    _description = 'Type'

    name = fields.Char("Scope")


class ProcurementData(models.Model):
    _name = 'procurement.data'
    _rec_name = 'name'
    _description = 'Procurement Data'

    name = fields.Char('Name')
    is_contractor = fields.Boolean('Is Contractor')
    is_installer = fields.Boolean('Is Installer')
