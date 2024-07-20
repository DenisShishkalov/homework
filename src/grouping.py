import json
import re
from collections import Counter


def grouping_operations(transactions: str, category: str) -> dict:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории.
    """
    with open(transactions, encoding='utf-8') as f:
        sentence = json.load(f)
        operations_ = []
        for i in sentence:
            if i.get('description'):
                operations_.append(i)
        result = [category for trans in operations_ if re.findall(category, trans['description'])]

        c = dict(Counter(result))
        return c

        # trans = []
        # for i in transaction_list:
        #     if i.get('descriptions'):
        #         trans.append(i)
        #     return trans
    # return [op for op in trans if re.search(category, op['descriptions'])]


if __name__ == '__main__':
    # list_category = ['Перевод организации, Открытие вклада, Перевод с карты на карту, Перевод с карты на счет']
    print(grouping_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', 'Перевод организации'))
    print(grouping_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', 'Перевод с карты на карту'))
    print(grouping_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', "Перевод с карты на счет"))
    print(grouping_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', "Открытие вклада"))
