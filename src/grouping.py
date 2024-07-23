import json
from collections import Counter

from config import file_transaction_json  # type: ignore


def grouping_operations(transactions: list[dict], category: list) -> dict:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории.
    """
    operations_ = []
    for i in transactions:
        if i.get('description'):
            operations_.append(i)
            result = [trans['description'] for trans in operations_ if trans['description'] in category]
            count_ = Counter(result)
            count_dict = dict(count_)
    return count_dict


if __name__ == '__main__':
    path = file_transaction_json
    with open(path, encoding='utf-8') as f:
        sentence = json.load(f)
    list_category = ['Перевод организации', 'Открытие вклада', 'Перевод с карты на карту', 'Перевод с карты на счет']
    grouping_operations(sentence, list_category)
