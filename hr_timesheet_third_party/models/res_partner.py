# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    third_party_timesheet_ids = fields.One2many('account.analytic.line', 'third_party_id')
    third_party_unit_amount_total = fields.Integer(string="Third Party Hours", compute="_compute_third_party_unit_amount_total")

    def _compute_third_party_unit_amount_total(self):
        for record in self:
            record.third_party_unit_amount_total = sum(record.third_party_timesheet_ids.mapped('unit_amount'))

    def action_third_party_timesheet(self):
        return {
            'name': _('Timesheet Activities'),
            'view_mode': 'tree,form',
            'res_model': 'account.analytic.line',
            'views': [
                (self.env.ref('hr_timesheet.hr_timesheet_line_tree').id, 'tree'),
                (self.env.ref('hr_timesheet.hr_timesheet_line_form').id, 'form'),
            ],
            'type': 'ir.actions.act_window',
            'domain': [('third_party_id', '=', self.id)]
        }
