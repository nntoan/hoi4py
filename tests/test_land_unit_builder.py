import unittest

from src.unit_builder.land_unit_builder import LandUnitBuilder


class LandUnitBuilderCase(unittest.TestCase):
    def test_init(self):
        builder = LandUnitBuilder("data/")

        self.assertIsNotNone(builder.units_dict)
