from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _name = 'res.config.settings'
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Dispatch Management System')