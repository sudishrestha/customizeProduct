# -*- coding: utf-8 -*-
from odoo import models,osv, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
class ProductCustomizeTask(models.Model):
	_inherit = 'product.template'
	donation = fields.Boolean('Donation')
