# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Adcement Stock",
    "version": "1.0",
    "depends": ["base","stock","adcement_purchase",],
    "author": "Mohamed Habib Challouf",
    "category": "purchase",
    "description": """
    This module provide stock : edit the lot and serial
    """,
    'data': ['res_partner_view.xml',
             'stock_view.xml',
             ],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}