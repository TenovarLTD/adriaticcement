# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Adcement Purchase",
    "version": "1.0",
    "depends": ["base","purchase"],
    "author": "Mohamed Habib Challouf",
    "category": "purchase",
    "description": """
    This module provide purchase : calendar view for vessel
    """,
    'data': ['purchase_order_line_view.xml','security/ir.model.access.csv'],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}