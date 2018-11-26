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
            'regiments': ['infantry'] * 11 + ['artillery_brigade'] * 6,
            'supports': ['engineer', 'recon', 'artillery'],
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
                    'soft_attack': [
                        +0.05 * 3,  # Infantry weapons
                        +0.2  # Superior Firepower
                    ],
                    'defense': [
                        +0.05 * 4  # Support weapons
                    ],
                    'breakthrough': [
                        +0.05 * 4  # Support weapons
                    ],
                },
                'artillery_brigade': {
                    'soft_attack': [
                        +0.1 * 3  # Artillery Upgrade
                    ],
                },
                'artillery': {
                    'soft_attack': [
                        -0.4,  # Support Companies
                        +0.1 * 3  # Artillery Upgrade
                    ],
                    'hard_attack': [
                        -0.4  # Support Companies
                    ],
                    'defense': [
                        -0.4  # Support Companies
                    ],
                    'breakthrough': [
                        -0.4  # Support Companies
                    ],
                },
                'engineer': {
                    'soft_attack': [
                        -0.5,  # Support Companies
                        +0.2  # Superior Firepower
                    ],
                    'defense': [
                        +0.1  # Support Companies
                    ],
                    'breakthrough': [
                        +0.5  # Support Companies
                    ],
                },
                'recon': {
                    'soft_attack': [
                        -0.9,  # Support Companies
                        +0.2  # Superior Firepower
                    ],
                    'hard_attack': [
                        -0.9  # Support Companies
                    ],
                    'defense': [
                        -0.5  # Support Companies
                    ],
                    'breakthrough': [
                        -0.5  # Support Companies
                    ],
                }
            }
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)

    def test_calculate_armor_stats(self):
        builder = LandDivisionBuilder("data/")
        division_template_dict = {
            'name': 'Test-Division',
            'division_names_group': 'Test_Arm_01',
            'regiments': ['light_armor'] * 10 + ['motorized'] * 10,
            'supports': ['engineer', 'recon', 'artillery'],
            'equipments': {
                'light_armor': ['light_tank_equipment_2'],
                'motorized': ['infantry_equipment_3', 'motorized_equipment_1'],
                'infantry': ['infantry_equipment_3'],
                'artillery_brigade': ['artillery_equipment_2'],
                'engineer': ['infantry_equipment_3', 'support_equipment_1'],
                'artillery': ['artillery_equipment_2'],
                'recon': ['infantry_equipment_3'],
                'anti_air': ['anti_air_equipment_1'],
                'anti_tank': ['anti_tank_equipment_1'],
            },
            'technologies': {
                'light_armor': {
                    'breakthrough': [
                        +0.2
                    ],
                },
                'motorized': {
                    'soft_attack': [
                        +0.05 * 2 + 0.1,  # Infantry weapons
                    ],
                    'defense': [
                        +0.05 * 4  # Support weapons
                    ],
                    'breakthrough': [
                        +0.05 * 4  # Support weapons
                    ],
                },
                'infantry': {
                    'soft_attack': [
                        +0.05 * 3,  # Infantry weapons
                    ],
                    'defense': [
                        +0.05 * 4  # Support weapons
                    ],
                    'breakthrough': [
                        +0.05 * 4  # Support weapons
                    ],
                },
                'artillery_brigade': {
                    'soft_attack': [
                        +0.1 * 3  # Artillery Upgrade
                    ],
                },
                'artillery': {
                    'soft_attack': [
                        -0.4,  # Support Companies
                        +0.1 * 3  # Artillery Upgrade
                    ],
                    'hard_attack': [
                        -0.4  # Support Companies
                    ],
                    'defense': [
                        -0.4  # Support Companies
                    ],
                    'breakthrough': [
                        -0.4  # Support Companies
                    ],
                },
                'engineer': {
                    'soft_attack': [
                        -0.5,  # Support Companies
                    ],
                    'defense': [
                        +0.1  # Support Companies
                    ],
                    'breakthrough': [
                        +0.5  # Support Companies
                    ],
                },
                'recon': {
                    'soft_attack': [
                        -0.9,  # Support Companies
                    ],
                    'hard_attack': [
                        -0.9  # Support Companies
                    ],
                    'defense': [
                        -0.5  # Support Companies
                    ],
                    'breakthrough': [
                        -0.5  # Support Companies
                    ],
                }
            }
        }
        result = builder.calculate_stats(division_template_dict)

        self.assertIsNotNone(result)
