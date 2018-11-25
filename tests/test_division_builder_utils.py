import unittest

from src.division_builder.utils import get_item_dict, list_item_path, get_item, trans_dict


class LandDivisionBuilderUtilsCase(unittest.TestCase):
    def test_get_item_dict(self):
        file_list = ['infantry.txt']
        root_path = 'data/'
        result = get_item_dict(root_path + "common/units/", file_list)

        self.assertTrue('infantry' in result.keys())

    def test_list_item_path(self):
        file_list = ['infantry.txt']
        root_path = 'data/'
        result = list_item_path(root_path + "common/units/", file_list)

        self.assertEqual(result[0], 'data/common/units/infantry.txt')

    def test_get_item(self):
        file_path = 'data/common/units/infantry.txt'
        result = get_item(file_path)

        self.assertTrue('infantry' in result.keys())

    def test_trans_dict(self):
        dict1 = {
            'recon': {
                'soft_attack': [-0.9, 0.2],
                'hard_attack': [-0.9],
                'defense': [-0.5],
                'breakthrough': [-0.5],
            }
        }

        dict2 = {
            'soft_attack': {
                'recon': [-0.9, 0.2]
            },
            'hard_attack': {
                'recon': [-0.9]
            },
            'defense': {
                'recon': [-0.5]
            },
            'breakthrough': {
                'recon': [-0.5]
            },
        }

        self.assertTrue(trans_dict(dict1), dict2)
        self.assertTrue(trans_dict(dict2), dict1)
