# -*- coding: utf-8 -*-

{
    'name': 'EcoGrip/Allied',
    'category': 'sale',
    'summary': 'EcoGrip/Allied',
    'version': '15.0.31',
    'author': "Mission Critical Inc",
    'website': "https://www.missioncriticalbps.com/",
    'description': """ EcoGrip/Allied """,
    'icon': '/allied_tus/static/description/icon.png',
    'depends': ['crm', 'crm_sales_estimate_customer', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_stage.xml',
        'data/product_demo.xml',
        'views/crm_lead_view.xml',
        'views/res_users.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
