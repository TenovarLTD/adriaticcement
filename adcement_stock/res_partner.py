# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _

class res_partner(models.Model):
    """ Inherits partner and adds driver information in the partner form """
    _inherit = 'res.partner'
    
    #Do not touch _name it must be same as _inherit
    #_name = 'openerpmodel'

    is_driver=fields.Boolean(string='Driver',help="is a driver")
                

