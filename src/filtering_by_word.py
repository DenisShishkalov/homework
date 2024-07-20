import json
import re


def filtered_operations(list_dict: str, search: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    with open(list_dict, encoding='utf-8') as f:
        data_ = json.load(f)
        operations_ = []
        for i in data_:
            if i.get('state'):
                operations_.append(i)
        return [trans for trans in operations_ if re.search(search, trans['state'])]


if __name__ == '__main__':

    filtered_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', 'CANCELED')
    filtered_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', 'PENDING')
    filtered_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', 'EXECUTED')
