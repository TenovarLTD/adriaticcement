# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2009-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Niyas Raphy(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Payment ',
    'summary': """Payment  with Paid Details""",
    'version': '0.3',
    'description': """""",
    'author': 'tenovar',
    'company': 'Tenovar',
    'website': 'http://www.tenovar.com',
    'category': 'Accounting',
    'depends': ['account','report'],
    'license': 'AGPL-3',
    'data': [
        'views/account_print_template.xml',
        'views/account_payment_print.xml',
        'views/receipt_payment.xml',
        #'views/report_invoice.xml'
             ],   
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': False,

}
