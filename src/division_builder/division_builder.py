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
        pass

    def calculate_stats(self, division_template_dict: dict) -> dict:
        stats_dict = {}  # type: dict
        for regiment in division_template_dict['regiments']:
            regiment_stat_dict = {}  # type: dict
            for stat in self.units_dict[regiment]:
                regiment_stat_dict[stat] = self.units_dict[regiment][stat]
            equipment_name = division_template_dict['equipments'][regiment]
            for stat in self.equipment_stats_dict[equipment_name]:
                regiment_stat_dict[stat] = self.equipment_stats_dict[equipment_name][stat]
            for item in regiment_stat_dict:
                if not item in stats_dict.keys():
                    stats_dict[item] = []
                stats_dict[item].append(regiment_stat_dict[item])

        for support in division_template_dict['supports']:
            support_stat_dict = {}  # type: dict
            for stat in self.units_dict[support]:
                support_stat_dict[stat] = self.units_dict[support][stat]
            equipment_name = division_template_dict['equipments'][support]
            for stat in self.equipment_stats_dict[equipment_name]:
                if not stat in support_stat_dict.keys():
                    support_stat_dict[stat] = self.equipment_stats_dict[equipment_name][stat]
                else:
                    support_stat = self.equipment_stats_dict[equipment_name][stat] * (1 + support_stat_dict[stat])
                    support_stat_dict[stat] = support_stat
            for item in support_stat_dict:
                if not item in stats_dict.keys():
                    stats_dict[item] = []
                stats_dict[item].append(support_stat_dict[item])

        _need = Counter({})  # type: Counter
        for item in stats_dict['need']:
            _need = _need + Counter(item)
        result = {
            'Max Speed': min(stats_dict['maximum_speed']),
            'HP': sum(stats_dict['max_strength']),
            'Organisation': sum(stats_dict['max_organisation'], 0.0) / len(stats_dict['max_organisation']),
            'Recovery Rate': sum(stats_dict['default_morale'], 0.0) / len(stats_dict['default_morale']),
            'Reconnaissance': 0,  # TODO
            'Suppression': sum(stats_dict['suppression']),
            'Weight': sum(stats_dict['weight']),
            'Supply use': sum(stats_dict['supply_consumption']),
            'Reliability': 0,  # TODO
            'Trickleback': 0,  # TODO
            'Exp. Loss': 0,  # TODO

            'Soft attack': sum(stats_dict['soft_attack']),
            'Hard attack': sum(stats_dict['hard_attack']),
            'Air attack': sum(stats_dict['air_attack']),
            'Defense': sum(stats_dict['defense']),
            'Breakthrough': sum(stats_dict['breakthrough']),
            'Armor': max(stats_dict['armor_value']) * 0.3 + sum(stats_dict['armor_value']) * 0.7,
            'Piercing': max(stats_dict['ap_attack']) * 0.4 + sum(stats_dict['ap_attack'], 0.0) / len(
                stats_dict['ap_attack']) * 0.6,
            'Entrenchment': 0,  # TODO
            'Eq. Capture Ratio': 0,  # TODO
            'Combat Width': sum(stats_dict['combat_width']),
            'Manpower': sum(stats_dict['manpower']),
            'Training Time': max(stats_dict['training_time']),
            'Need': dict(_need)

        }
        return result
