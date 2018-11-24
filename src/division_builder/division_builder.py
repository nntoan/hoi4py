from collections import Counter

from src.division_builder.utils import get_item_dict


class LandDivision:
    def __init__(self, division_template_dict: dict):
        self.division_template_dict = division_template_dict


class LandDivisionBuilder:
    def __init__(self, root_path: str):
        units_file_list = ['anti_tank.txt', 'anti_tank_brigade.txt', 'anti-air.txt', 'anti-air_brigade.txt',
                           'artillery.txt',
                     'artillery_brigade.txt', 'cavalry.txt', 'engineer.txt', 'field_hospital.txt', 'heavy_armor.txt',
                     'infantry.txt', 'logistics.txt', 'maintenance.txt', 'medium_armor.txt', 'military_police.txt',
                     'modern_armor.txt', 'recon.txt', 'signal.txt', 'sp_anti-air_brigade.txt',
                           'sp_artillery_brigade.txt', 'super_heavy_armor.txt', 'tank_destroyer_brigade.txt']
        self.units_dict = get_item_dict(root_path + "common/units/", units_file_list)
        equipment_file_list = ['anti_air.txt', 'anti_tank.txt', 'artillery.txt',
                               'guided_missiles.txt', 'infantry.txt', 'mechanized.txt',
                               'motorized.txt', 'support.txt', 'tank_heavy.txt', 'tank_light.txt',
                               'tank_medium.txt', 'tank_modern.txt', 'tank_super_heavy.txt']
        equipment_dict = get_item_dict(root_path + "common/units/equipment/", equipment_file_list)
        self.equipment_stats_dict = {}  # type: dict

        equipment_stat_list = ['maximum_speed', 'reliability', 'defense', 'breakthrough', 'hardness', 'armor_value',
                               'soft_attack', 'hard_attack', 'ap_attack', 'air_attack', 'build_cost_ic', 'resources',
                               'archetype', 'priority', 'visual_level']

        for equipment in equipment_dict:
            if equipment[-1:].isdigit():
                _dict = equipment_dict[equipment[:-2]].copy()
                _dict.update(equipment_dict[equipment])
                for item in set(_dict.keys()) - set(equipment_stat_list):
                    _dict.pop(item)
                self.equipment_stats_dict[equipment] = _dict

    def calculate_stats(self, division_template_dict: dict) -> dict:
        stats_dict = {}  # type: dict
        battalion_types = ['regiments', 'supports']
        for battalion_type in battalion_types:
            for battalion in division_template_dict[battalion_type]:
                stat_dict = {}  # type: dict
                for stat in self.units_dict[battalion]:
                    stat_dict[stat] = self.units_dict[battalion][stat]
                equipment_name = division_template_dict['equipments'][battalion]
                for stat in self.equipment_stats_dict[equipment_name]:
                    if not stat in stat_dict.keys():
                        stat_dict[stat] = self.equipment_stats_dict[equipment_name][stat]
                    else:
                        stat_dict[stat] = self.equipment_stats_dict[equipment_name][stat] * (1 + stat_dict[stat])
                for item in stat_dict:
                    if not item in stats_dict.keys():
                        stats_dict[item] = []
                    stats_dict[item].append(stat_dict[item])


        _need = Counter({})  # type: Counter
        for item in stats_dict['need']:
            _need = _need + Counter(item)
        round_degree = 5
        result = {
            'Max Speed': round(min(stats_dict['maximum_speed']), round_degree),
            'HP': round(sum(stats_dict['max_strength']), round_degree),
            'Organisation': round(sum(stats_dict['max_organisation'], 0.0) / len(stats_dict['max_organisation']),
                                  round_degree),
            'Recovery Rate': round(sum(stats_dict['default_morale'], 0.0) / len(stats_dict['default_morale']),
                                   round_degree),
            'Reconnaissance': 0,  # TODO
            'Suppression': round(sum(stats_dict['suppression']), round_degree),
            'Weight': round(sum(stats_dict['weight']), round_degree),
            'Supply use': round(sum(stats_dict['supply_consumption']), round_degree),
            'Reliability': 0,  # TODO
            'Trickleback': 0,  # TODO
            'Exp. Loss': 0,  # TODO

            'Soft attack': round(sum(stats_dict['soft_attack']), round_degree),
            'Hard attack': round(sum(stats_dict['hard_attack']), round_degree),
            'Air attack': round(sum(stats_dict['air_attack']), round_degree),
            'Defense': round(sum(stats_dict['defense']), round_degree),
            'Breakthrough': round(sum(stats_dict['breakthrough']), round_degree),
            'Armor': round(max(stats_dict['armor_value']) * 0.3 + sum(stats_dict['armor_value']) * 0.7, round_degree),
            'Piercing': round(max(stats_dict['ap_attack']) * 0.4 + sum(stats_dict['ap_attack'], 0.0) / len(
                stats_dict['ap_attack']) * 0.6, round_degree),
            'Entrenchment': 0,  # TODO
            'Eq. Capture Ratio': 0,  # TODO
            'Combat Width': round(sum(stats_dict['combat_width']), round_degree),
            'Manpower': round(sum(stats_dict['manpower']), round_degree),
            'Training Time': round(max(stats_dict['training_time']), round_degree),
            'Need': dict(_need)

        }
        return result
