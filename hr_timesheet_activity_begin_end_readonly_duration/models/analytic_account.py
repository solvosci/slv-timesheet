# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, api
from datetime import timedelta


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    unit_amount = fields.Float(readonly=True)

    @api.constrains("time_start", "time_stop")
    def _check_time_start_stop(self):
        for line in self:
            line.onchange_hours_start_stop()
        super(AccountAnalyticLine, self)._check_time_start_stop()
