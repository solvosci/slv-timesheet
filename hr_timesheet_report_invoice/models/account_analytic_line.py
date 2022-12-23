# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"
    
    def get_invoice_name(self):
        """
        Obtains invoice number from timesheets if all the timesheets belong
        to the same invoice
        """
        timesheets_w_inv = self.filtered(lambda x: x.timesheet_invoice_id)
        return (
            len(timesheets_w_inv.mapped("timesheet_invoice_id")) == 1
            and len(timesheets_w_inv) == len(self)
            and timesheets_w_inv[0].timesheet_invoice_id.name
            or False
        )
