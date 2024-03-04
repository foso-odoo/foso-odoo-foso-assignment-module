from odoo import fields,models,api

class FleetVehicleModelCategory(models.Model):

    _name = 'dock.model'

    name = fields.Char(string="Name")
   
