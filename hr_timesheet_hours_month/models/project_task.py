# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    planned_hours_year = fields.Boolean(default=False)

    remaining_hours_month = fields.Float(compute='_compute_remaining_hours_month', compute_sudo=True)

    def _compute_remaining_hours_month(self):
        n_month = fields.Date.today().month
        for record in self:
            if record.planned_hours_year:
                record.remaining_hours_month = record.remaining_hours - (record.planned_hours - (n_month * (record.planned_hours / 12)))
            else:
                record.remaining_hours_month = 0.0
    
    def name_get(self):
        if self.env.context.get('hr_timesheet_display_remaining_hours'):
            name_mapping = dict(super().name_get())
            for task in self.filtered(lambda x: x.allow_timesheets and x.planned_hours_year):
                hours, mins = (str(int(duration)).rjust(2, '0') for duration in divmod(abs(task.remaining_hours_month) * 60, 60))
                hours_left = _(
                    "(%(sign)s%(hours)s:%(minutes)s monthly)",
                    sign='-' if task.remaining_hours_month < 0 else '',
                    hours=hours,
                    minutes=mins,
                )
                name_mapping[task.id] = name_mapping.get(task.id, '') + u"\u00A0" + hours_left
            return list(name_mapping.items())
        return super().name_get()
