from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float('Volume', compute='_compute_volume')
    
    @api.depends('move_line_ids.product_id.volume', 'move_line_ids.quantity')
    def _compute_volume(self):
        for picking in self:
            picking_volume = sum(
                line.product_id.volume * line.quantity for line in picking.move_line_ids
            )
            picking.volume = picking_volume
