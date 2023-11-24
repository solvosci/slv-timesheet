# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _order = 'date desc, sequence, id desc'

    sequence = fields.Integer(default=10)
