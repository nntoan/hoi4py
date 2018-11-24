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
            'regiments': ['infantry'] * 1 + ['artillery_brigade'] * 1,
            'supports': ['engineer', 'recon'],
            'equipments': {
                'infantry': ['infantry_equipment_3'],
                'artillery_brigade': ['artillery_equipment_2'],
                'engineer': ['infantry_equipment_3', 'support_equipment_1'],
                'artillery': ['artillery_equipment_2'],
                'recon': ['infantry_equipment_3'],
                'anti_air': ['anti_air_equipment_1'],
                'anti_tank': ['anti_tank_equipment_1'],
            },
            'technologies': {
                'infantry': {
                    'soft_attack': [0.05, 0.05, 0.05, 0.2],
                    'defense': [0.05, 0.05, 0.05, 0.05],
                    'breakthrough': [0.05, 0.05, 0.05, 0.05],
                },
                'artillery_brigade': {
                    'soft_attack': [0.1, 0.1, 0.1],
                },
                'artillery': {
                    'soft_attack': [0.1, 0.1, 0.1, 0.2],
                },
                'engineer': {
                    'soft_attack': [-0.5, 0.2],
                    'defense': [0.1],
                    'breakthrough': [0.5],
                },
                'recon': {
                    'soft_attack': [-0.9, 0.2],
                    'hard_attack': [-0.9],
                    'defense': [-0.5],
                    'breakthrough': [-0.5],
                }
            }
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)
