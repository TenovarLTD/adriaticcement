# -*- coding: utf-8 -*-


{
    'name': 'Sales Fixed commissions by pricelist',
    'version': '10.0.1.0.0',
    'author': 'TenovarLtd',
    'category': 'Sales',
    'website': 'https://tenovar.com',
    'license': 'AGPL-3',
    'depends': [
        'sale_commission','sale','product',
    ],
    'data': [
        'views/product_pricelist_view.xml',
        'views/sale_order_view.xml',
        'data/sale_commission_demo.xml',
    ],
    'installable': True,
}
