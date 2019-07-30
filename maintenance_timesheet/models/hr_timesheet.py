from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    maintenance_request_id = fields.Many2one(
        string='Maintenance request',
        comodel_name='maintenance.request')
