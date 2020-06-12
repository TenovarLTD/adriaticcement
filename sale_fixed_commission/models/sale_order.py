# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    is_product = fields.Boolean(default=False)
    object_pricelist = fields.Many2one(
        comodel_name="sale.order.line.pricelist.commission",
        ondelete="restrict"        
    )
   
    @api.multi
    def _get_commission_from_pricelist(self):
        #self.ensure_one()
        if  not self.order_id.pricelist_id:
            return False      
        rule = self.order_id.pricelist_id #self.env['product.pricelist.item'].browse(rule_id)
        return rule.commission_id

    @api.onchange('product_id')
    def _onchange_sale_product_pricelist(self):
        product =self.product_id
        if product :
            self.is_product = True
            #self.env.cr.execute("DELETE from sale_order_line_pricelist_commission where not id = 1 and current_user = %s ",% (self._uid))
         
            self.env.cr.execute("DELETE from sale_order_line_pricelist_commission where not id = 1 and user_current = %s "% (self._uid))
            #self._cr.fetchall()
        commission  = self._get_commission_from_pricelist()
        pricelist =  self.order_id.pricelist_id
        if pricelist :
            #self.is_product = True        
            self.env['sale.order.line.pricelist.commission'].create({'user_current' :self._uid ,'is_pricelist' : True,'pricelist_id': self.order_id.pricelist_id.id,'commission':commission.id,'agent' : self.agents.agent.id})
            
            
class SaleOrderLineCommission(models.Model):    
    _name = 'sale.order.line.pricelist.commission'

    user_current = fields.Many2one('res.users','Current User')     
    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist',ondelete='cascade')
    commission = fields.Many2one(
        comodel_name="sale.commission",
        ondelete="restrict",         
    )
    agent = fields.Many2one(
        comodel_name="res.partner",         
        ondelete="restrict",       
    )
    is_pricelist = fields.Boolean()

class SaleOrderLineAgent(models.Model):
    _inherit = "sale.order.line.agent","sale.commission.line.mixin"
    _name = "sale.order.line.agent"
 
    @api.onchange('agent')
    def onchange_agent(self):
        res = super(SaleOrderLineAgent,self).onchange_agent()  
        last_idd = self.env['sale.order.line.pricelist.commission'].search([('user_current','=',self._uid)])
        if last_idd :
            last_id = last_idd[-1]
            if last_id.is_pricelist == False :
                #self.env.cr.execute("DELETE from sale_order_line_pricelist_commission where not id = 1 and not id = %d" % (last_id.id))
                raise UserError(_('Please check Pricelist . thank you !'))
            else :                    
                self.commission = last_id.commission
        else :
            raise UserError(_('Please check Pricelist . thank you !'))
        return res

    