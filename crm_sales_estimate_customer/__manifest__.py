# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Pipeline with Sales Estimate',
    'version': '1.1.2',
    'currency': 'EUR',
    'price': 19.0,
    'license': 'Other proprietary',
    'category': 'Sales/Sales',
    'summary': """CRM Pipeline / Lead with Sales Estimate""",
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/cse.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/crm_sales_estimate_customer/1212',
    'depends': [
        'odoo_sale_estimates',
        'crm',
        ],
    'description': """
CRM Pipeline / Lead with Sales Estimate
    """,
    'data':[
        'security/ir.model.access.csv',
        'wizard/crm_sale_estimate_view.xml',
        'views/sale_estimate_view.xml',
        'views/crm_lead_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
