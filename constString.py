import json

with open(".\constString.json",'r',encoding='UTF-8') as load_f:
    language_info = json.load(load_f)
# print(language_info['default_language'])

default_language = language_info['default_language']

def get_item(item_str):
    index = language_info["language_kinds"][default_language]
    # print(language_info[item_str + "_" + str(index)])
    return language_info[item_str + "_" + str(index)]

def get_language_list():
    result = []
    for key in language_info["language_kinds"].keys():
        result.append(key)
    # print(result)
    return result