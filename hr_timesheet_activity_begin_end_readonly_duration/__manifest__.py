# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Timesheet Activities - Begin/End Hours - Readonly Duration",
    "summary": """
        Change the readonly attribute of field unit_amount to true
        to force the Begin Hour and End Hour to be added
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-timesheet",
    "depends": ["hr_timesheet_activity_begin_end"],
    "data": ["views/hr_timesheet_views.xml"],
    'installable': True,
}
