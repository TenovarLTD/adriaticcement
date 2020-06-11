
# -*- encoding: utf-8 -*-
##############################################################################
#
#     
#        Tenovar LTD, <Mohamed Habib Challouf>,Code Management Solution
#    Copyright (C) 2016-2017 Tiny SPRL (http://tenovar.com). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Stock Report",
    "version": "9.0",
    "depends": ["base","stock","adcement_stock"],
    "category": "stock",
    "description": """
    This module provide :specific report for picking operation and delivery slip
    """,
    "init_xml": [],
    'data': ['deliveryslip.xml','report_stockpicking_operations.xml','stock_view.xml','mail_template_data.xml'
             #'picking_operation.xml'
             #,'delivery_slip.xml'
             ],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}