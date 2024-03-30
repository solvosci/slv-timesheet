# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models
from odoo.osv import expression


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.onchange("project_id")
    def _onchange_project_id(self):
        res = super()._onchange_project_id()
        if self.project_id:
            task_domain = res["domain"]["task_id"]
            res["domain"]["task_id"] = expression.OR([
                task_domain,
                [
                    ("project_id", "=", self.project_id.id),
                    ("stage_id", "=", False),
                ]
            ])
        return res
