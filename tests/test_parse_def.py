import unittest

import pyparsing

from src.hoi4_parsing.parse_def import CurlyDict, Date, Dictionary, Float, Identifier, Integer, List, String


def assert_for_dict_equal(self, parse_result: pyparsing.ParseResults, assert_dict: dict, ):
    for item in assert_dict:
        if isinstance(assert_dict[item], list):
            assert_data = parse_result[item].asList()
        elif isinstance(assert_dict[item], dict):
            assert_data = parse_result[item].asDict()
        else:
            assert_data = parse_result[item]
        self.assertEqual(assert_data, assert_dict[item])


class PrimitiveCase(unittest.TestCase):

    def test_identifier(self):
        test_string = '''A_valid_3_identifier'''

        result = Identifier.parseString(test_string)
        self.assertEqual(result[0], 'A_valid_3_identifier')

    def test_positive_integer(self):
        test_string = '''1234'''

        result = Integer.parseString(test_string)
        self.assertEqual(result[0], 1234)

    def test_negative_integer(self):
        test_string = '''-1234'''

        result = Integer.parseString(test_string)
        self.assertEqual(result[0], -1234)

    def test_positive_float(self):
        test_string = '''12.234'''

        result = Float.parseString(test_string)
        self.assertEqual(result[0], 12.234)

    def test_negative_float(self):
        test_string = '''-12.234'''

        result = Float.parseString(test_string)
        self.assertEqual(result[0], -12.234)

    def test_date(self):
        test_string = '''1454.4.28'''

        result = Date.parseString(test_string)
        self.assertEqual(result[0], '1454.4.28')

    def test_utf8_string(self):
        test_string = '"Östergötland"'

        result = String.parseString(test_string)
        self.assertEqual(result[0], "Östergötland")


class ComplexTypCase(unittest.TestCase):

    def test_curly_dict(self):
        test_string = '''{
                id=4597
                type=4713
            }'''

        result = CurlyDict.parseString(test_string)
        self.assertEqual(result["id"], 4597)

    def test_dict(self):
        test_string = '''
            date="1454.1.1"
            thing="stuff"
            one=1'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["thing"], "stuff")
        self.assertEqual(result["one"], 1)

    def test_curly_brace_sub_dict(self):
        test_string = '''player="TUR"
            savegame_version=
            {
                first=1
                second=7
                third=3
                forth=0
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["savegame_version"]["second"], 7)

    def test_curly_dict_in_value(self):
        test_string = '''player={
                savegame_version=
                {
                    first=1
                    second=7
                    third=3
                    forth=0
                }
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["player"]["savegame_version"]["second"], 7)

    def test_list_of_numbers(self):
        test_string = '''1 2 0 0 0 0 0 1 0 1 0 0'''

        result = List.parseString(test_string)
        self.assertEqual(result[1], 2)

    def test_list_of_identifiers(self):
        test_string = '''first second third'''

        result = List.parseString(test_string)
        self.assertEqual(result[1], "second")

    def test_list_of_dates(self):
        test_string = '''1454.1.1 2020.1.5 1550.3.4'''

        result = List.parseString(test_string)
        self.assertEqual(result[1], "2020.1.5")

    def test_curly_list_of_identifiers(self):
        test_string = '''gameplaysettings=
            {
                setgameplayoptions=
                {
                   first=1
                   second=1
                   third=1
                }
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["gameplaysettings"]["setgameplayoptions"]["second"], 1)

    def test_curly_brace_sub_list(self):
        test_string = '''gameplaysettings=
            {
                setgameplayoptions=
                {
                    1 4 0 0 0 0 0 1 0 1 0 0 
                }
            }'''

        result = Dictionary.parseString(test_string)

        self.assertEqual(result["gameplaysettings"]["setgameplayoptions"][1], 4)

    def test_province_int_as_key(self):
        test_string = '''-1=
            {
                name="Stockholm"
                owner="SWE"
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["-1"]["name"], "Stockholm")

    def test_mixed_type_dictionary(self):
        test_string = '''history=
            {
                manpower=3.000
                fort1=yes
                capital="Stockholm"
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["history"]["manpower"], 3)
        self.assertEqual(result["history"]["fort1"], True)
        self.assertEqual(result["history"]["capital"], "Stockholm")

    def test_date_as_key(self):
        test_string = '''1438.3.6=
            {
                controller="SWE"
            }'''

        result = Dictionary.parseString(test_string)
        self.assertEqual(result["1438.3.6"]["controller"], "SWE")

    def test_hoi4_common_unit(self):
        test_string = '''
infantry = {
    sprite = infantry
    map_icon_category = infantry
    
    priority = 600
    ai_priority = 200
    active = no

    type = {
        infantry
    }
    
    group = infantry
    
    categories = {
        category_front_line
        category_light_infantry
        category_all_infantry
        category_army
    }
    
    combat_width = 2
    
    #Size Definitions
    max_strength = 25
    max_organisation = 60
    default_morale = 0.3
    manpower = 1000

    #Misc Abilities
    training_time = 90
    suppression = 1
    weight = 0.5
    
    supply_consumption = 0.07

    need = {
        infantry_equipment = 100
    }
}
        '''
        result = Dictionary.parseString(test_string)
        assert_dict = {
            "sprite": "infantry",
            "priority": 600,
            "ai_priority": 200,
            "active": False,
            "type": "infantry",
            "group": "infantry",
            "categories": ['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'],
            "combat_width": 2,
            "max_strength": 25,
            "max_organisation": 60,
            "default_morale": 0.3,
            "manpower": 1000,
            "training_time": 90,
            "suppression": 1,
            "weight": 0.5,
            "supply_consumption": 0.07,
            "need": {"infantry_equipment": 100}
        }
        assert_for_dict_equal(self, result['infantry'], assert_dict)
