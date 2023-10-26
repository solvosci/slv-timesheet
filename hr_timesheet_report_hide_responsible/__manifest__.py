# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Timesheet Report Hide Responsible",
    "summary": """
        Adds a report that hides the responsible
        users column if there is only one.
    """,
    "version": "12.0.1.0.0",
    "license": "LGPL-3",
    "category": "Human Resources",
    "author": "Solvos",
    "website": "https://github.com/solvosci/slv-timesheet",
    "depends": [
        "hr_timesheet",
    ],
    "data": [
        "report/hr_timesheet_report.xml",
    ],
}
