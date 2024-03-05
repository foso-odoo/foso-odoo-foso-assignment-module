from odoo import fields, models ,api

class StockPicking(models.Model):
    _inherit = 'stock.picking.batch'
    

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    doc_id = fields.Many2one('dock.model',string='Dock')
    # print(scheduled_date)

    #max_weight =fields.Float()
    

    
    total_weight = fields.Float(string='Weight', compute='_compute_total_weight', store=True)
    total_volume = fields.Float(string='Volume', compute='_compute_total_volume', store=True)

    @api.depends('picking_ids.move_line_ids.product_id.weight', 'picking_ids.move_line_ids.quantity')
    def _compute_total_weight(self):
        for batch in self:
            #print("Scheduled_date",batch.scheduled_date)
            total_weight = 0
            for picking in batch.picking_ids:
                picking_weight = sum(
                    line.product_id.weight * line.quantity for line in picking.move_line_ids
                )
                total_weight += picking_weight
            if batch.vehicle_id.category_id.max_weight != 0:
                batch.total_weight = total_weight/batch.vehicle_id.category_id.max_weight
            else :
                batch.total_weight = 0
                
            
            
    @api.depends('picking_ids.move_line_ids.product_id.volume', 'picking_ids.move_line_ids.quantity')
    def _compute_total_volume(self):
        for batch in self:
            total_volume = 0
            for picking in batch.picking_ids:
                picking_volume = sum(
                    line.product_id.volume * line.quantity for line in picking.move_line_ids
                )
                total_volume += picking_volume
            if batch.vehicle_id.category_id.max_volume != 0:
                batch.total_volume = total_volume/batch.vehicle_id.category_id.max_volume
            else :
                batch.total_volume = 0
    
    