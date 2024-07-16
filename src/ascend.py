import csv


def reader_csv_file(file: str) -> None:
    """
    Функция, считывающая информацию из csv файла
    """
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=";")
        next(reader)
        for row in reader:
            print(row)


reader_csv_file(r"C:\Users\Денис\Downloads\transactions.csv")
