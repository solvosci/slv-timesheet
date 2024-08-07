# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, _
from odoo.exceptions import ValidationError

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def copy(self, default=None):
        if self.employee_id:
            raise ValidationError(
                    _("You cannot duplicate timesheet")
                )
        return super().copy(default=default)
