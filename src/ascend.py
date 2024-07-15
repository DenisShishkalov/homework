import csv


def reader_csv_file(file: str):
    with open(file) as f:
        reader = csv.reader(f)
        return reader


print(reader_csv_file(r'C:\Users\Денис\Downloads\transactions.csv'))

