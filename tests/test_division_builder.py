import unittest

from src.division_builder.division_builder import LandDivisionBuilder
from src.division_builder.technologies import technologies, equipments


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
            'regiments': ['infantry'] * 11 + ['artillery_brigade'] * 6,
            'supports': ['engineer', 'recon', 'artillery', 'anti_air', 'anti_tank'],
            'equipments': equipments,
            'technologies': technologies,
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)

    def test_calculate_armor_stats(self):
        builder = LandDivisionBuilder("data/")
        division_template_dict = {
            'name': 'Test-Division',
            'division_names_group': 'Test_Arm_01',
            'regiments': ['light_armor'] * 10 + ['motorized'] * 10,
            'supports': ['engineer', 'recon', 'artillery', 'anti_air', 'anti_tank'],
            'equipments': equipments,
            'technologies': technologies,
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)
