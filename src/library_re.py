import json
import re


def filtered_trans(list_dict: list[dict], search: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    with open(list_dict, encoding='utf-8') as f:
       str_ = f.read()
        # data_ = json.load()
    #     for i in data_:
    #         if i.get('description'):
    #             return i
    #
    #         pattern = re.search()


    pattern = re.compile(search)
    split_text = pattern.split(str_)

    print((split_text))



info = r'C:\Users\Денис\PycharmProjects\01\data\operations.json'

print(filtered_trans(info, 'Перевод организации'))
