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
    "name":'Account Remittance Advice',
    "version": "1.0",
    "depends": ["base",'report','account'],
    "author": "Mohamed Habib Challouf",
    "category": "Account",
    "description": """
    This module provide : Print Remittance Advice Report

Use this App to print remittance advice report and send to your supplier by email directly.
    """,
    "init_xml": [],
    'data': ['report/template_remittance_advice.xml','report/report_remittance_advice.xml',],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}