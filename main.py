import os

import pandas as pd

from src.grouping import grouping_operations


def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """

    # Программа приветствует пользователя:

    global sorted_dictionary_list
    greeting_user = '''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню : 
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла 
    3. Получить информацию о транзакциях из XLSX-файла'''

    user_choice_file = input(f'{greeting_user}\n')
    while user_choice_file not in ['1', '2', '3']:
        print("Некорректный ввод, попробуйте снова")
        user_choice_file = input()

    else:
        if user_choice_file == '1':
            print('Для обработки выбран JSON-файл.')
            from src.utils import get_info
            read_file = get_info(r"C:\Users\Денис\PycharmProjects\01\data\operations.json")
        elif user_choice_file == '2':
            print('Для обработки выбран CSV-файл.')
            from src.ascend import reader_csv_file
            read_file = reader_csv_file(r'C:\Users\Денис\Downloads\transactions.csv')
        elif user_choice_file == '3':
            print('Для обработки выбран XLSX-файл.')
            from src.reader_xlsx import reading_a_file
            read_file = reading_a_file(pd.read_excel(r"C:\Users\Денис\Downloads\transactions_excel.xlsx"))

    choice_filter = '''\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    user_choice_filter = input(f'{choice_filter}\n').upper()

    while user_choice_filter not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус операции {user_choice_filter} недоступен. \n{choice_filter}")
        user_choice_filter = input().upper()
        break
    else:
        from src.filtering_by_word import filtered_operations
        tran_filtered = filtered_operations(r"C:\Users\Денис\PycharmProjects\01\data\operations.json",
                                            f'{user_choice_filter}')
        result = tran_filtered
        print(result)
        print(f'\nОперации отфильтрованы по статусу {user_choice_filter}')

    # После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю,
    # и выводит в консоль операции, соответствующие выборке пользователя:

    while True:
        user_choice_sorted_date = input('Отсортировать операции по дате? Да/Нет\n').lower()
        if user_choice_sorted_date == "да":
            user_choice_sorted_increasing_decreasing = input("""Отсортировать: 
                  1. По возрастанию
                  2. По убыванию \n""")
            if user_choice_sorted_increasing_decreasing == "1":
                sorted_dictionary_list = sorted(result, key=lambda d: d.get("date"), reverse=False)
            elif user_choice_sorted_increasing_decreasing == '2':
                sorted_dictionary_list = sorted(result, key=lambda d: d.get("date"), reverse=True)
            break
        elif user_choice_sorted_date == "нет":
            sorted_dictionary_list = result
            break

        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")
            continue

    while True:
        question_currency = input("Выводить только рублевые транзакции? Да/Нет\nВвод: ").lower()
        if question_currency == "да":
            new_list_sort = []
            for i in sorted_dictionary_list:
                if i.get('code') == "RUB":
                    new_list_sort.append(i)
            break
        if question_currency == "нет":
            new_list_sort = sorted_dictionary_list
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову описании? Да/Нет\nВвод: ").lower()
        if question_description == "да":
            question_description_word = input("Введите слово: ")
            last_filter = grouping_operations(new_list_sort, question_description_word)
            print(last_filter)
            break
        elif question_description == "нет":
            last_filter = new_list_sort
            print(last_filter)
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue

    print('Распечатываю итоговый список транзакций... \n'
          f'Всего банковских операций в выборке: {len(last_filter)}\n')



if __name__ == '__main__':
    main()
