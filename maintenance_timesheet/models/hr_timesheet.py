from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    maintenance_request_id = fields.Many2one(
        string='Maintenance request',
        comodel_name='maintenance.request')

    @api.onchange('maintenance_request_id')
    def onchange_maintenance_request_id(self):
        if self.maintenance_request_id and not self.project_id:
            self.project_id = self.maintenance_request_id.project_id
            self.task_id = self.maintenance_request_id.task_id
