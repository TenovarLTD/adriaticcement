# -*- coding: utf-8 -*-
from odoo import http,__init__
from odoo.http import request

class helpdesk_website((http.Controller)):
    @http.route('/helpdesk',auth='user',website=True)
    def support_helpdesk(self,**kargs):
        return request.render('project_helpdesk.helpdesk')