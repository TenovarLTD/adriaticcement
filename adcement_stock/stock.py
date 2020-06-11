# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from collections import namedtuple
import json
import time

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare
from odoo.addons.procurement.models import procurement
from odoo.exceptions import UserError




class PackOperationLot(models.Model):
    _inherit= "stock.pack.operation.lot"
    _description = "Lot/Serial number for pack ops"
    
    lot_name = fields.Char('Voyage Number' ,size=2)
    arrived_date=fields.Date(string='BOL' , help='bill of lading',default=fields.Date.context_today)
    vessel_id=fields.Many2one('vessel.vessel',string='Vessel')


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'
    
    vessel_id=fields.Many2one('vessel.vessel',string='Vessel')



class Picking(models.Model):
    _inherit = "stock.picking"
    
    
    truck_driver=fields.Many2one('res.partner',string='Truck Driver', domain=[('is_driver','=',True)],states={'done': [('readonly', True)]},)
    truck_number=fields.Char('Truck Number', size=64,states={'done': [('readonly', True)]},)
    trailer_number=fields.Char('Trailer Number', size=64,states={'done': [('readonly', True)]},)
    weight_certirtificat_number=fields.Float('Weight Certificate Number',)
    
    
   

    def _create_lots_for_picking(self):
            Lot = self.env['stock.production.lot']
            for pack_op_lot in self.mapped('pack_operation_ids').mapped('pack_lot_ids'):
                if not pack_op_lot.lot_id:
                    if pack_op_lot.arrived_date and pack_op_lot.vessel_id:
                        lot = Lot.create({'name': pack_op_lot.lot_name +' / '+pack_op_lot.vessel_id.name+' / '+str(pack_op_lot.arrived_date),'vessel_id': pack_op_lot.vessel_id.id,'product_id': pack_op_lot.operation_id.product_id.id})
                    else:   
                        lot = Lot.create({'name': pack_op_lot.lot_name, 'product_id': pack_op_lot.operation_id.product_id.id})
                    pack_op_lot.write({'lot_id': lot.id})
            # TDE FIXME: this should not be done here
            self.mapped('pack_operation_ids').mapped('pack_lot_ids').filtered(lambda op_lot: op_lot.qty == 0.0).unlink()
            #create_lots_for_picking = _create_lots_for_picking