import os

from src.vanilla_parsing.parse_def import Dictionary


def get_item_dict(root_path: str, file_list: list) -> dict:
    file_path_list = list_item_path(root_path, file_list)
    item_dict = {}
    for file_path in file_path_list:
        item_dict.update(get_item(file_path))

    return item_dict


def list_item_path(root_path: str, file_list: list) -> list:
    path_list = []
    for item in file_list:
        path_list.append(os.path.join(root_path, item))

    return path_list


def get_item(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf_8_sig') as file:
        str_ = file.read()
    res = Dictionary.parseString(str_)
    res_dict = {k: v.asDict() for k, v in res[0].items()}

    return res_dict