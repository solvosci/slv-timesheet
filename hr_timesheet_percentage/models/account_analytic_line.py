# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    timesheet_pct = fields.Float(
        readonly=True,
        string="Timesheets percentage",
        help="""
        For aggregate values, shows percentage of these timesheets
        """,
    )

    @api.model
    def read_group(
        self,
        domain,
        fields,
        groupby,
        offset=0,
        limit=None,
        orderby=False,
        lazy=True
    ):
        res = super().read_group(
            domain,
            fields,
            groupby,
            offset=offset,
            limit=limit,
            orderby=orderby,
            lazy=lazy
        ) 
        fields = [x.split(":")[0] for x in fields]
        # When empty,
        # - for tree view, res = []
        # - for pivot view, res has a unique record (dict) with "__count" = 0
        # When filled,
        # - for tree view, res has many records, without "__count" value
        #   (no head record)
        # - for kanban view, res has a first head record with "__count" > 0
        if (
            "timesheet_pct" in fields
            and len(res) > 0
            and res[0].get("__count", 1) > 0
        ):
            # TODO verify if it should be calculated when not found
            total_unit_amount = sum(
                line.get("unit_amount", 0.0)
                for line in res
            )
            for line in res:
                line["timesheet_pct"] = (
                    0.0 if total_unit_amount == 0.0
                    else line.get("unit_amount", 0.0) / total_unit_amount
                )

        return res
