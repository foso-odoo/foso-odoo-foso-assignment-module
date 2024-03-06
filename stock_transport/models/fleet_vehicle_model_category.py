from odoo import fields,models,api

class FleetVehicleModelCategory(models.Model):

    _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string="Max Weight(kg)")
    max_volume = fields.Float(string="Max Volume(m\xb3)")


    def _compute_display_name(self):
        for category in self:
             category.display_name = "%s (%.2f kg, %.2f m\xb3)" % (
                category.name,
                category.max_weight,
                category.max_volume
             )
