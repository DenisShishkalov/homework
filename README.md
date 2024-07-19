# Homework_Project

## Homework_10_1 Продвинутый Git

### Задачи

1. Создайте GitHub-репозиторий.
2. Залейте текущий проект в GitHub-репозиторий.
3. Создайте модуль processing для новых функций.
4. Напишите функцию, которая принимает на вход список словарей и значение для ключа
   state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список, содержащий только те
   словари, у которых ключ state содержит переданное в функцию значение.
5. Напишите функцию, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари
   отсортированы по убыванию даты (ключ
   date). Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).
6. Создайте README-файл для проекта.

#### Пример работы функции

1. Вход функции
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

2. Выход функции со статусом по умолчанию EXECUTED
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

3. Выход функции, если вторым аргументов передано 'CANCELED'
   [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

4. Вход функции
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

5. Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

## Homework_10_2 Тестирование. Pytest

## Тестирование проекта

### Задачи

1. Напишите тестовые функции с использованием библиотеки pytest для существующего кода проекта.
2. Используйте фикстуры для формирования входных данных для тестов.
3. Используйте параметризацию в тестах для запуска одного теста с различным набором входных параметров.
4. Добейтесь покрытия тестами минимум 80% кода.

## Homework_11_1 Включения и генераторы

### Задачи

1. Создайте модуль `generators` для новых функций.
2. Реализуйте функцию, которая принимает список словарей с банковскими операциями (или объект-генератор, который выдает
   по одной банковской операции) и возвращает итератор, который выдает по очереди операции, в которых указана заданная
   валюта.

- Пример вызова функции:

`usd_transactions = filter_by_currency(transactions, "USD")`
`for _ in range(2):
print(next(usd_transactions)["id"])`

- Пример вывода:

`939719570`

`142264268`

3. Напишите генератор, который принимает список словарей и возвращает описание каждой операции по очереди.

- Пример вызова функции:

`descriptions = transaction_descriptions(transactions)`

`for _ in range(5):
print(next(descriptions))`

- Пример вывода:

`Перевод организации`

`Перевод со счета на счет`

`Перевод со счета на счет`

`Перевод с карты на карту`

`Перевод организации`

4. Напишите генератор номеров банковских карт, который должен генерировать номера карт в формате `XXXX XXXX XXXX XXXX`,
   где `X` — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например от `0000 0000 0000 0001`
   до `9999 9999 9999 9999` (диапазоны передаются как параметры генератора).

- Пример вызова функции:

`for card_number in card_number_generator(1, 5):
print(card_number)`

`0000 0000 0000 0001`
`0000 0000 0000 0002`
`0000 0000 0000 0003`
`0000 0000 0000 0004`
`0000 0000 0000 0005`

## Homework_11_2 Декораторы

### Задачи

1. Создайте модуль `decorators`, в котором будут располагаться декораторы.
2. Напишите декоратор `log` , который будет логировать вызов функции и ее результат в файл или в консоль.
   Декоратор `log` принимает один необязательный аргумент `filename` , который определяет путь к файлу, в который будут
   записываться логи. Если `filename` не задан, то логи будут выводиться в консоль. Если вызов функции закончился
   ошибкой,
   то записывается сообщение об ошибке и входные параметры функции.

- Пример использования:

`@log(filename="mylog.txt")
def my_function(x, y):
return x + y
my_function(1, 2)`

В результате выполнения функции `my_function(1, 2)`будет возвращено значение `3`, а в лог-файл mylog.txt будет
записано сообщение в следующем формате: `my_function ok`. Если в процессе выполнения функции произошла ошибка,
то в лог-файл будет записано сообщение в формате:
`my_function error: <тип ошибки>. Inputs: (1, 2), {}` Где `<тип ошибки>`заменяется на текст ошибки, а
`(1, 2)` и `{}`— на значения позиционных и именованных аргументов функции соответственно.

3. Напишите тесты на pytest для декоратора`log` .

## Homework_12_1 Библиотеки json, requests и datetime

### Задачи

1. Реализуйте функцию, которая принимает на вход путь до `JSON`-файла и возвращает список словарей с данными о
   финансовых
   транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список. Функцию поместите
   в модуль `utils`. Файл с данными о финансовых транзациях `operations.json` поместите в директорию `data/` в корне
   проекта.

Ссылка на файл: `operations.json.`

2. Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции `(amount)` в рублях, тип
   данных —
   `float`. Если транзакция была в `USD` или `EUR`, происходит обращение к внешнему API для получения текущего курса
   валют и конвертации суммы операции в рубли. Для
   конвертации валюты воспользуйтесь `Exchange Rates Data API: https://apilayer.com/exchangerates_data-api`. Функцию
   конвертации поместите в модуль`external_api`.
   - Используйте переменные окружения из файла `.env` для сокрытия чувствительных данных (токенов доступа для API).
   - Создайте шаблон файла .env и разместите в репозитории на GitHub.
   - Напишите тесты для новых функций, используйте Mock и patch.


## 12.2 Библиотека logging

### Задачи

   1. Создайте логеры для перечисленных модулей:
      - `masks`
      - `utils`.
   2. Реализуйте запись логов в файл. Логи должны записываться в папку `logs` в корне проекта. Файлы логов должны иметь
   расширение `.log`.
   3. Формат записи лога в файл должен включать метку времени, название модуля, уровень серьезности и сообщение, 
   описывающее события или ошибки, которые произошли.
   4. Лог должен перезаписываться при каждом запуске приложения.

## 13.1 Библиотеки csv и pandas

### Задачи

-  Реализовать считывание финансовых операций из `CSV-` и `XLSX`-файлов.

#### Дополнительное задание
- Типизируйте написанный код и добейтесь того, чтобы `mypy`при запуске не выдавал ошибок.
- Напишите тесты для новых функций.
Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.


## 13.2. Библиотеки re, collections, random

### Задачи
- Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
а возвращать список словарей, у которых в описании есть данная строка. При реализации этой функции можно использовать
библиотеку `re` для работы с регулярными выражениями.

Расположение новой функции в структуре проекта определите самостоятельно.
- Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий
операций, а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
в каждой категории.
Категории операций хранятся в поле `description`. Расположение новой функции в структуре проекта
определите самостоятельно.

- Напишите функцию `main` в модуле `main`, которая отвечает за основную логику проекта
и связывает функциональности между собой.