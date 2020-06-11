# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import api, fields, models, _, SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.tools.translate import _
from openerp.tools.float_utils import float_is_zero, float_compare
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError, AccessError
from datetime import datetime, timedelta


class vessel_vessel(models.Model):
    _name = 'vessel.vessel'
    _description = 'Vessel'
    
    name=fields.Char('Vessel Name', size=64, required=False, readonly=False)
            

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    
    vessel_id=fields.Many2one('vessel.vessel',string='Vessel')
    
   
    
    
    
    
    
    
 