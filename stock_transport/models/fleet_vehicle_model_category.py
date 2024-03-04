from odoo import fields,models,api

class FleetVehicleModelCategory(models.Model):

    _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string="Max Weight(kg)" , default=0)
    max_volume = fields.Float(string="Max Volume", default=0)

    # @api.depends('offer_ids')
    # def _compute_best_price(self):
    #     for rec in self:
    #         rec.best_price = max(rec.offer_ids.mapped('price') , default=0)
    def _compute_display_name(self):
        for category in self:
             category.display_name = "%s (%.2f, %.2f)" % (
                category.name,
                category.max_weight,
                category.max_volume
             )
