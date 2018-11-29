import unittest

from src.land_warfare.land_warfare_calc import get_damage_of_avoid_hit, get_hits, calc_damage
from src.utils import sum_for_result_with_func


class LandLandWarfareCalcCase(unittest.TestCase):
    def test_get_damage_of_avoid_hit(self):
        dice_size, chance_to_avoid_hit, damage_modifier = 4, 90, 0.05
        result = get_damage_of_avoid_hit(dice_size, chance_to_avoid_hit, damage_modifier)

        self.assertIsNotNone(result)

    def test_get_hits(self):
        sa_or_ha, def_or_bt = 100, 10
        hits_at_def, hits_at_no_def = get_hits(sa_or_ha, def_or_bt)

        self.assertTrue(hits_at_def == def_or_bt and hits_at_no_def == sa_or_ha - def_or_bt)

    def test_sum_for_result_with_func(self):
        dice_size, chance_to_avoid_hit, damage_modifier, n = 4, 90, 0.05, 100
        result = sum_for_result_with_func(get_damage_of_avoid_hit,
                                          dice_size,
                                          chance_to_avoid_hit,
                                          damage_modifier,
                                          n=100)

        self.assertTrue(result > (1 * (100 - chance_to_avoid_hit) / 100 * 0.05) * n)
        self.assertTrue(result < (dice_size * (100 - chance_to_avoid_hit) / 100 * 0.05) * n)

    def test_calc_damage(self):
        a = {
            'Armor': 0.0,
            'Breakthrough': 0.0,
            'Defense': 0.0,
            'HP': 0.0,
            'Hard attack': 0.0,
            'Hardness': 0.0,
            'Name': 'Test-Division_a',
            'Organisation': 0.0,
            'Piercing': 0.0,
            'Priority': {'medium_armor': 1},
            'Soft attack': 1000,
        }
        b = {
            'Armor': 0.0,
            'Breakthrough': 0.0,
            'Defense': 500,
            'HP': 0.0,
            'Hard attack': 0.0,
            'Hardness': 0.0,
            'Name': 'Test-Division_b',
            'Organisation': 0.0,
            'Piercing': 0.0,
            'Priority': {'infantry': 1},
            'Soft attack': 0.0,
        }
        c = {
            'Armor': 0.0,
            'Breakthrough': 0.0,
            'Defense': 2000,
            'HP': 0.0,
            'Hard attack': 0.0,
            'Hardness': 0.0,
            'Name': 'Test-Division_c',
            'Organisation': 0.0,
            'Piercing': 0.0,
            'Priority': {'infantry': 1},
            'Soft attack': 0.0,
        }

        result = calc_damage(a, b, 'Defense')

        self.assertIsNotNone(result)

        result = calc_damage(a, c, 'Defense')

        self.assertIsNotNone(result)
