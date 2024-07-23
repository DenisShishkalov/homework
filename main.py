from typing import Any

from src.config import file_transaction_csv, file_transaction_json
from src.filtering_by_word import filtered_by_descriptions
from src.processing import filter_by_state
from src.widget import mask_account_card, get_data
from src.utils import get_info
from src.ascend import reader_csv_file
from src.reader_xlsx import reading_a_file, ret


def main() -> Any:
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """

    # Программа приветствует пользователя:

    greeting_user = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню :
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла'"""

    user_choice_file = input(f'{greeting_user}\n')
    while user_choice_file not in ['1', '2', '3']:
        print("Некорректный ввод, попробуйте снова")
        user_choice_file = input()

    else:
        if user_choice_file == '1':
            print('Для обработки выбран JSON-файл.')
            full_file = get_info(file_transaction_json)  # Для обработки выбран JSON-файл (file_transaction_json путь
            # к файлу взят из config.py)
        elif user_choice_file == '2':
            print('Для обработки выбран CSV-файл.')
            full_file = reader_csv_file(file_transaction_csv)  # Для обработки выбран CSV-файл.
        elif user_choice_file == '3':
            print('Для обработки выбран XLSX-файл.')  # Для обработки выбран XLSX-файл.'
            full_file = reading_a_file(ret)
    # print(full_file)
    choice_filter = '''\nВведите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''  # Фильтрация по статусу
    user_choice_filter = input(f'{choice_filter}\n').upper()

    while user_choice_filter not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус операции {user_choice_filter} недоступен. \n{choice_filter}")
        user_choice_filter = input().upper()
        break
    else:
        first_filter = filter_by_state(full_file, f'{user_choice_filter}')
        # print(first_filter)
        print(f'\nОперации отфильтрованы по статусу {user_choice_filter}')
    # После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю,
    # и выводит в консоль операции, соответствующие выборке пользователя:

    while True:
        user_choice_sorted_date = input('Отсортировать операции по дате? Да/Нет\n').lower()
        if user_choice_sorted_date == "да":
            user_choice_sorted_increasing_decreasing = input('Отсортировать: '
                                                             '1. По возрастанию'
                                                             '2. По убыванию \n')
            if user_choice_sorted_increasing_decreasing == "1":
                second_filter = sorted(first_filter, key=lambda d: d.get("date"), reverse=False)
            elif user_choice_sorted_increasing_decreasing == '2':
                second_filter = sorted(first_filter, key=lambda d: d.get("date"), reverse=True)
            break
        elif user_choice_sorted_date == "нет":
            second_filter = first_filter  # отфильтрованный 2 раз основной список транзкций
            break

        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")
            continue
    while True:
        question_currency = input("Выводить только рублевые транзакции? Да/Нет\nВвод: ").lower()
        if question_currency == "да":
            third_filter = [trans for trans in second_filter
                            if trans.get('code') == 'RUB' or trans.get('currency_code') == 'RUB']
            break
        if question_currency == "нет":
            third_filter = second_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue
    # print(third_filter)

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВвод: ").lower()
        if question_description == "да":
            question_description_word = input("Введите слово: ").capitalize()
            last_filter = filtered_by_descriptions(third_filter, f'{question_description_word}')
            # print(last_filter)
            break
        elif question_description == "нет":
            last_filter = third_filter
            # print(last_filter)
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue

    print('Распечатываю итоговый список транзакций... \n'
          f'Всего банковских операций в выборке: {len(last_filter)}\n')
    if len(last_filter) != 0:
        for trans in last_filter:
            if trans["description"] in "Открытие вклада" in trans["description"]:
                print(f"{get_data(trans.get("date"))} Открытие вклада\n{mask_account_card(trans.get("to"))}"
                      f"\nСумма:{trans.get('amount')}\n")
            else:
                print(f"{get_data(trans.get('date'))} {trans.get("description")}\n{mask_account_card(trans["from"])}"
                      f" -> {mask_account_card(trans.get('to'))}\nСумма: {trans.get('amount')}"
                      f" {trans.get('code') or trans.get('currency_code')}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == '__main__':
    main()
