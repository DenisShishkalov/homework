import json
import re
from collections import defaultdict

from typing import Any


def grouping_operations(transactions: str, category: str) -> Any:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории.
    """
    with open(transactions, encoding='utf-8') as f:
        sentence = json.load(f)

        def_dict = defaultdict(list)

        for k, v in sentence:
            def_dict['description'].append(v)
            print(def_dict)







        # trans = []
        # for i in transaction_list:
        #     if i.get('descriptions'):
        #         trans.append(i)
        #     return trans
    # return [op for op in trans if re.search(category, op['descriptions'])]





if __name__ == '__main__':
    list_category = 'Перевод организации'
    # list_category = ['Перевод организации', 'Открытие вклада', 'Перевод с карты на карту', 'Перевод с карты на счет']
    print(grouping_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', list_category))