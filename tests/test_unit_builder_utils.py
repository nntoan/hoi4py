import unittest

from src.unit_builder.utils import get_item_dict, list_item_path, get_item


class LandUnitBuilderCase(unittest.TestCase):
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
