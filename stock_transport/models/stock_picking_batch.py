from odoo import fields, models ,api

class StockPicking(models.Model):
    _inherit = 'stock.picking.batch'
    

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle',store = True)
    category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category',store = True)
    doc_id = fields.Many2one('dock.model',string='Dock')
    transfers = fields.Integer('Transfers',compute='_compute_transfers',store = True)
    lines = fields.Integer('Lines',compute='_compute_lines',store = True)

    

    
    total_weight = fields.Float(string='Weight', compute='_compute_total_weight', store=True)
    total_volume = fields.Float(string='Volume', compute='_compute_total_volume', store=True)
    temp_weight = fields.Float(string='weight' ,compute='_compute_total_weight', store=True)
    temp_volume = fields.Float(string='volume' ,compute='_compute_total_volume',store=True)

    @api.depends('picking_ids.move_line_ids.product_id.weight', 'picking_ids.move_line_ids.quantity')
    def _compute_total_weight(self):
        for batch in self:
            temp_weight = 0 
            for picking in batch.picking_ids:
                picking_weight = sum(
                line.product_id.weight * line.quantity for line in picking.move_line_ids
                )
                temp_weight += picking_weight

            if batch.category_id.max_weight != 0:
                batch.total_weight = temp_weight / batch.category_id.max_weight
            else:
                batch.total_weight = 0

            batch.temp_weight = temp_weight  

                
            
            
    @api.depends('picking_ids.move_line_ids.product_id.volume', 'picking_ids.move_line_ids.quantity')
    def _compute_total_volume(self):
        for batch in self:
            temp_volume = 0
            for picking in batch.picking_ids:
                picking_volume = sum(
                    line.product_id.volume * line.quantity for line in picking.move_line_ids
                )
                temp_volume += picking_volume
                
            if batch.category_id.max_volume != 0:
                batch.total_volume = temp_volume/batch.category_id.max_volume
            else :
                batch.total_volume = 0
                
            batch.temp_volume = temp_volume
            # print(batch.temp_volume)
                
    
    @api.depends('picking_ids')
    def _compute_transfers(self):
        for batch in self:
            transfers = len(batch.picking_ids)
            
    @api.depends('picking_ids.move_line_ids')
    def _compute_lines(self):
        for batch in self:
            lines = len(batch.picking_ids.move_line_ids)
            
            
    
            
    