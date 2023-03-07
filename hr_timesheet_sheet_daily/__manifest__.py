# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Hr Timesheet Sheet Daily",
    "summary": """
        Adds change the workflow of timesheet sheets to work only with one date
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-timesheet",
    "depends": ["hr_timesheet_sheet"],
    "data": [
        "views/hr_timesheet_sheet_views.xml",
        "views/res_config_settings.xml"
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}
