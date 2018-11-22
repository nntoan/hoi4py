import unittest

from src.division_builder.division_builder import LandDivisionBuilder


class LandDivisionBuilderCase(unittest.TestCase):
    def test_init(self):
        builder = LandDivisionBuilder("data/")

        self.assertIsNotNone(builder.units_dict)
        self.assertIsNotNone(builder.equipment_stats_dict)

    def test_calculate_stats(self):
        builder = LandDivisionBuilder("data/")
        division_template_dict = {
            'name': 'Test-Division',
            'division_names_group': 'Test_Arm_01',
            'regiments': ['infantry'] * 7 + ['artillery_brigade'] * 2,
            'support': ['engineer'],
            'equipments': {
                'infantry': 'infantry_equipment_1',
                'artillery_brigade': 'artillery_equipment_1'
            }
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)
