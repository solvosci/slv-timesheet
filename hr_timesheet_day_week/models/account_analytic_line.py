from odoo import api, fields, models

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"
    day_week = fields.Selection([
        ("0", "Monday"),
        ("1", "Tuesday"),
        ("2", "Wednesday"),
        ("3", "Thursday"),
        ("4", "Friday"),
        ("5", "Saturday"),
        ("6", "Sunday")],
        compute="_compute_week_day", store=True, string="Day of week")

    @api.depends('date')
    def _compute_week_day(self):
        for record in self:
            week_day = record.date.weekday()
            record.day_week = str(week_day)
