from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # FIXME incorrect comodel_name
    maintenance_request_id = fields.Many2one(string='Maintenance request',
                                             comodel_name='maintenance_request')

    # TODO employee validation when maintenance_request id is filled
