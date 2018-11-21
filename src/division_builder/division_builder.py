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
        self.equipment_stats_dict = {}

        for equipment in equipment_dict:
            if equipment[-1:].isdigit():
                _dict = equipment_dict[equipment[:-2]].copy()
                _dict.update(equipment_dict[equipment])
                self.equipment_stats_dict[equipment] = _dict
        pass

    def calculate_stats(self, division_template_dict: dict) -> dict:
        stats = {}
        # for regiment in division_template_dict['regiments']:
        #     for stat in self.units_dict[regiment]:
        #         stats[stat] += stat
        return stats
