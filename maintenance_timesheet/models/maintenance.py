from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    project_id = fields.Many2one(string='Project',
                                 comodel_name='project.project',
                                 ondelete='restrict')
    create_project_from_equipment = fields.Boolean(default=True)

    @api.model
    def create(self, values):
        if values.get('create_project_from_equipment'):
            new_project = self.env['project.project'].create({
                'name': values.get('name'),
                'allow_timesheets': True})
            values['project_id'] = new_project.id
        return super(MaintenanceEquipment, self).create(values)

    def _create_new_request(self, date):
        new_request = \
            super(MaintenanceEquipment, self)._create_new_request(date)
        if self.project_id and not new_request.project_id:
            new_request.project_id = self.project_id
        return new_request


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    project_id = fields.Many2one(string='Project',
                                 comodel_name='project.project',
                                 domain=[('allow_timesheets', '=', True)])
    task_id = fields.Many2one(string='Task',
                              comodel_name='project.task')
    timesheet_ids = fields.One2many(string='Timesheets',
                                    comodel_name='account.analytic.line',
                                    inverse_name='maintenance_request_id')
    timesheet_total_hours = fields.Float(
        compute='_compute_timesheet_total_hours')

    @api.depends('timesheet_ids.unit_amount')
    def _compute_timesheet_total_hours(self):
        for request in self:
            request.timesheet_total_hours = \
                sum(request.timesheet_ids.mapped('unit_amount'))

    @api.onchange('equipment_id')
    def onchange_equipment_id(self):
        super(MaintenanceRequest, self).onchange_equipment_id()
        if self.equipment_id and self.equipment_id.project_id:
            self.project_id = self.equipment_id.project_id

    def action_view_timesheet_ids(self):
        self.ensure_one()
        action = self.env.ref(
            'maintenance_timesheet.timesheet_action_from_request').read()[0]
        action['domain'] = [('maintenance_request_id', '=', self.id)]
        action['context'] = {
            'default_project_id': self.project_id.id,
            'default_task_id': self.task_id.id,
            'default_maintenance_request_id': self.id
        }
        return action
