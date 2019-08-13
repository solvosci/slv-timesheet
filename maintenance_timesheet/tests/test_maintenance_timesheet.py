import odoo.tests.common as test_common
from odoo import fields
from datetime import timedelta


class TestMaintenanceTimesheet(test_common.TransactionCase):

    def setUp(self):
        super().setUp()

        self.cron = self.env.ref('maintenance.maintenance_requests_cron')
        self.project1 = self.env['project.project'].create({
            'name': 'My project',
            'allow_timesheets': True})

        self.equipment1 = self.env['maintenance.equipment'].create({
            'name': 'My equipment',
            'create_project_from_equipment': True,
            'maintenance_team_id':
                self.env.ref('maintenance.equipment_team_metrology').id,
            'period': 30,
            'maintenance_duration': 1.0})
        self.equipment2 = self.env['maintenance.equipment'].create({
            'name': 'My equipment without project',
            'create_project_from_equipment': False})
        self.equipment3 = self.env['maintenance.equipment'].create({
            'name': 'My equipment with related project',
            'create_project_from_equipment': False,
            'project_id': self.project1.id
        })

    def test_maintenance_equipment_project(self):
        self.assertEqual(self.equipment1.name, self.equipment1.project_id.name)
        self.assertFalse(self.equipment2.project_id)
        self.assertEqual(self.equipment3.project_id, self.project1)

    def test_generate_requests(self):
        self.cron.method_direct_trigger()

        generated_requests = self.env['maintenance.request'].search(
            [('equipment_id', '=', self.equipment1.id)])

        for req in generated_requests:
            self.assertEqual(req.project_id, req.equipment_id.project_id)

    # TODO account.analytic.line & demo data tests
