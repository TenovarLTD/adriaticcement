# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    commission = fields.Many2one( comodel_name="sale.commission", ondelete="restrict", related='pricelist_id.commission_id',readonly=True)
               
   
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _name = "sale.order.line"
      
    commission = fields.Many2one( comodel_name="sale.commission", ondelete="restrict",readonly=True)  

class SaleOrderLineAgent(models.Model):
    _inherit = "sale.order.line.agent"
    _name = "sale.order.line.agent"
    
    """
    commission = fields.Many2one(
        comodel_name="sale.commission",
        ondelete="restrict",
        required=True,
        store=True,
        related='object_id.commission'
    )   
    """ 
    
    @api.onchange('agent')
    def onchange_agent(self): 
        res = super(SaleOrderLineAgent,self).onchange_agent() 
        self.commission = self.object_id.commission        
        return res