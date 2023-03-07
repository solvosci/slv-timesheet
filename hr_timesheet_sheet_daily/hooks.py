# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    logging.getLogger('odoo.addons.hr_timesheet_daily').info(
        'Change sheet range setting')

    env = api.Environment(cr, SUPERUSER_ID, {})
    env.company.sheet_range = 'DAILY'