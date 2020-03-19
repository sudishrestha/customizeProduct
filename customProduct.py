# -*- coding: utf-8 -*-
from osv import fields, osv
class customProduct(osv.osv):
	_inherit = 'product.product'
	_columns = {
	'donation': fields.boolean('Donation', store=True),
	'mohpEM' : fields.boolean('MOHP Essesntial Medicine'),
	'govtSupply' : fields.boolean('Government Supply'),
	'orphanDrug' : fields.boolean('Orphan Drug'),
	'dentalItem' : fields.boolean('Dental Item')
	}
	default ={
	'legacy_projects_id' :0
	}
customProduct()
