from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float('Volume', compute='_compute_volume')

    @api.depends('product_id.volume')
    def _compute_volume(self):
        for record in self:
            record.volume = record.product_id.volume
