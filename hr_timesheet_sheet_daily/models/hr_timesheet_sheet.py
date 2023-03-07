# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet.sheet"

    date_end = fields.Date(
        related="date_start",
        states={"new": [("readonly", True)]},
        store=True,
    )
