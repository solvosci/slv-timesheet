from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


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

    @api.model
    def create(self, values):
        if values.get('maintenance_request_id'):
            self._check_request_done(values.get('maintenance_request_id'))
        return super(AccountAnalyticLine, self).create(values)

    @api.multi
    def write(self, values):
        if 'maintenance_request_id' in values \
                and values.get('maintenance_request_id'):
            self._check_request_done(values.get('maintenance_request_id'))
        return super(AccountAnalyticLine, self).write(values)

    def _check_request_done(self, request_id):
        """
        Creating or moving a timesheet to a finished request is forbidden.
        Anyway, modifying data of an existing one is still allowed
        """
        if self.env['maintenance.request'].browse(request_id).stage_id.done:
            raise ValidationError(
                _('Cannot save a timesheet to a maintenance '
                  'request already done'))
