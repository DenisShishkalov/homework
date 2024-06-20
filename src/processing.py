def filter_by_state(dictionary_list: list, state: str = 'EXECUTED') -> list:
    """ Принимает список словарей, и возвращает новый список
     у которых ключ state содержит переданное в функцию значение."""
    new_list_ = []

    for i in dictionary_list:
        if i.get("state") == state:
            new_list_.append(i)
    return new_list_


print(filter_by_state(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(dictionary_list: list, reverse_dictionary_list: bool = False) -> list:
    """ Функция сортировки операций по дате (по возрастанию) """
    sorted_dictionary_list = sorted(dictionary_list, key=lambda d: d.get('date'), reverse=reverse_dictionary_list)

    return sorted_dictionary_list


# print(sort_by_date(
#     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
