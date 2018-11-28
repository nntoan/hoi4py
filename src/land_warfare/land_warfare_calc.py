import random

from src.division_builder.division_builder import LandDivisionBuilder

LAND_COMBAT_ORG_DICE_SIZE = 4
LAND_COMBAT_STR_DICE_SIZE = 2

LAND_COMBAT_ORG_ARMOR_ON_SOFT_DICE_SIZE = 6
LAND_COMBAT_STR_ARMOR_ON_SOFT_DICE_SIZE = 2

LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.05
LAND_COMBAT_ORG_DAMAGE_MODIFIER = 0.05

LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR = 0.5
LAND_COMBAT_ORG_ARMOR_DEFLECTION_FACTOR = 0.5
BASE_CHANCE_TO_AVOID_HIT = 90
CHANCE_TO_AVOID_HIT_AT_NO_DEF = 60

armor_list = ['medium_armor']

builder = LandDivisionBuilder("data/")


def get_damage_of_avoid_hit(dice_size, chance_to_avoid_hit):
    return random.randint(1, dice_size) * (100 - chance_to_avoid_hit) / 100 * LAND_COMBAT_ORG_DAMAGE_MODIFIER


def get_hits(sa_or_ha: int, def_or_bt: int) -> (int, int):
    hit_at_def = 0
    hit_at_no_def = 0
    if sa_or_ha <= def_or_bt:
        hit_at_def = sa_or_ha
        hit_at_no_def = 0
    elif sa_or_ha > def_or_bt:
        hit_at_def = def_or_bt
        hit_at_no_def = sa_or_ha - def_or_bt
    return round(hit_at_def), round(hit_at_no_def)


def sum_for_result_with_func(func, *avgs, n: int):
    _list = []
    for i in range(n):
        _list.append(func(*avgs))
    result = sum(_list)

    return result


def calc_damage(a, b, def_type):
    atk_sa = round(a['Soft attack'] / 10)
    atk_ha = round(a['Hard attack'] / 10)
    def_ = round(b[def_type] / 10)
    a_division_type = max(a['Priority'], key=a['Priority'].get)
    b_division_type = max(b['Priority'], key=b['Priority'].get)

    org_soft_dice_size = LAND_COMBAT_ORG_DICE_SIZE
    org_hard_dice_size = LAND_COMBAT_ORG_DICE_SIZE
    if a_division_type in armor_list and a['Armor'] >= b['Piercing']:
        org_soft_dice_size = LAND_COMBAT_ORG_ARMOR_ON_SOFT_DICE_SIZE

    org_chance_to_avoid_hit_at_def = BASE_CHANCE_TO_AVOID_HIT
    org_chance_to_avoid_hit_at_no_def = CHANCE_TO_AVOID_HIT_AT_NO_DEF

    soft_hits = round(atk_sa * (1 - b['Hardness']))
    hard_hits = round(atk_ha * b['Hardness'])
    total_hits = soft_hits + hard_hits
    hits_at_def, hits_at_no_def = get_hits(total_hits, round(def_))

    soft_hits_at_def = round(hits_at_def / total_hits * soft_hits)
    hard_hits_at_def = round(hits_at_def / total_hits * hard_hits)
    soft_hits_at_no_def = round(hits_at_no_def / total_hits * soft_hits)
    hard_hits_at_no_def = round(hits_at_no_def / total_hits * hard_hits)

    org_soft_damage_at_def = sum_for_result_with_func(get_damage_of_avoid_hit,
                                                      org_soft_dice_size,
                                                      org_chance_to_avoid_hit_at_def,
                                                      n=soft_hits_at_def)
    org_hard_damage_at_def = sum_for_result_with_func(get_damage_of_avoid_hit,
                                                      org_hard_dice_size,
                                                      org_chance_to_avoid_hit_at_def,
                                                      n=hard_hits_at_def)
    org_soft_damage_at_no_def = sum_for_result_with_func(get_damage_of_avoid_hit,
                                                         org_soft_dice_size,
                                                         org_chance_to_avoid_hit_at_no_def,
                                                         n=soft_hits_at_no_def)
    org_hard_damage_at_no_def = sum_for_result_with_func(get_damage_of_avoid_hit,
                                                         org_hard_dice_size,
                                                         org_chance_to_avoid_hit_at_no_def,
                                                         n=hard_hits_at_no_def)

    org_damage = org_soft_damage_at_def + org_hard_damage_at_def + org_soft_damage_at_no_def + org_hard_damage_at_no_def

    return org_damage
