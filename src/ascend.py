import csv


def reader_csv_file(file: str) -> list:
    """
    Функция, считывающая информацию из csv файла
    """
    with open(file, encoding='utf-8') as f:
        csv.DictReader(f, delimiter=";")
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)
