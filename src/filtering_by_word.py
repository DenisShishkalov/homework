import json
import re


def filtered_operations(list_dict: list[dict], search: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    operations_ = []
    for i in list_dict:
        if i.get('description'):
            operations_.append(i)
    return [trans for trans in operations_ if re.search(search, trans['description'])]


if __name__ == '__main__':
    path = r'..\data\operations.json'
    with open(path, encoding='utf-8') as f:
        data_ = json.load(f)
        search_string = 'Перевод организации'
    filtered_operations(data_, search_string)
