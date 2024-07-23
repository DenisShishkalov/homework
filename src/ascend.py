import csv
from config import file_transaction_csv  # type: ignore


def reader_csv_file(file: str) -> list:
    """
    Функция, считывающая информацию из csv файла
    """
    with open(file, encoding='utf-8') as f:
        csv.DictReader(f, delimiter=";")
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


reader_csv_file(file_transaction_csv)
# print(reader_csv_file(file_transaction_csv))
