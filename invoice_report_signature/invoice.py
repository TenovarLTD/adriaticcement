# -*- coding: utf-8 -*-


from openerp import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice' 
    #Do not touch _name it must be same as _inherit
    #_name = 'account.invoice'
    total_payment = fields.Monetary(string='Total Payment', compute='_compute_payment', store=False, help="total payment.")
    
    @api.one
    @api.depends('amount_total','residual')
    def _compute_payment(self):
        total_payment=0.0
        
        for line in self.payment_ids:
            total_payment+=line.amount
        self.total_payment=total_payment
            
