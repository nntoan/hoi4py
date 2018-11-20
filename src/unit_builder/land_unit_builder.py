from src.unit_builder.utils import get_item_dict


class LandUnitBuilder:
    def __init__(self, root_path):
        file_list = ['anti_tank.txt', 'anti_tank_brigade.txt', 'anti-air.txt', 'anti-air_brigade.txt', 'artillery.txt',
                     'artillery_brigade.txt', 'cavalry.txt', 'engineer.txt', 'field_hospital.txt', 'heavy_armor.txt',
                     'infantry.txt', 'logistics.txt', 'maintenance.txt', 'medium_armor.txt', 'military_police.txt',
                     'modern_armor.txt', 'recon.txt', 'signal.txt', 'sp_anti-air_brigade.txt',
                     'sp_artillery_brigade.txt',
                     'super_heavy_armor.txt', 'tank_destroyer_brigade.txt']
        self.units_dict = get_item_dict(root_path + "common/units/", file_list)
