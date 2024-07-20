import pandas as pd
#
#
# from src.ascend import reader_csv_file
# from src.filtering_by_word import filtered_operations
# from src.reader_xlsx import reading_a_file
# from src.utils import get_info


def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """

    # Программа приветствует пользователя:

    greeting_user = '''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню: 
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
            get_info(r"C:\Users\Денис\PycharmProjects\01\data\operations.json")
        elif user_choice_file == '2':
            print('Для обработки выбран CSV-файл.')
            from src.ascend import reader_csv_file
            reader_csv_file(r'C:\Users\Денис\Downloads\transactions.csv')
        elif user_choice_file == '3':
            print('Для обработки выбран XLSX-файл.')
            from src.reader_xlsx import reading_a_file
            reading_a_file(pd.read_excel(r"C:\Users\Денис\Downloads\transactions_excel.xlsx"))

    choice_filter = '''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    user_choice_filter = input(f'{choice_filter}\n').upper()

    while user_choice_filter not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус операции {user_choice_filter} недоступен. \n{choice_filter}")
        user_choice_filter = input().upper()
    else:
        from src.filtering_by_word import filtered_operations
        print(filtered_operations(r'C:\Users\Денис\PycharmProjects\01\data\operations.json', f'{user_choice_filter}'))
        print(f'Операции отфильтрованы по статусу {user_choice_filter}')

    # После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю,
    # и выводит в консоль операции, соответствующие выборке пользователя:

    user_choice_sorted_date = input('Программа: Отсортировать операции по дате? Да/Нет\n').lower()
    if user_choice_sorted_date == "да":
        user_choice_sorted_increasing_decreasing = input("""Отсортировать: 
              1. По возрастанию
              2. По убыванию? \n""")
        if user_choice_sorted_increasing_decreasing == "1":
            from src.processing import sort_by_date
            sort_by_date(filtered_operations, False)

    else:
        user_choice_sorted_rub = input('Выводить только рублевые тразакции? Да/Нет\n').lower()
        if user_choice_sorted_rub == 'да':
            from src.generators import filter_by_currency
            filter_by_currency('RUB')


if __name__ == '__main__':
    main()