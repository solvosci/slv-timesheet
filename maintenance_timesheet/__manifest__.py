# © 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Bridge between Maintenance and Timesheets",
    "author": "Solvos Consultoría Informática",
    "version": "12.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/solvosci/slv-timesheet",
    "depends": [
        "maintenance",
        "hr_timesheet",
    ],
    "data": [
        # TODO hr_timesheet views??
        "views/maintenance.xml",
    ],
    # TODO demo data
    "license": 'AGPL-3',
    'installable': True,
}
