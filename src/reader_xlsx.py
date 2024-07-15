import pandas as pd


def reading_a_file(df: pd.DataFrame):
    """
    Функция считывания информации из xlsx файла
    """
    return df.sort_values(by='currency_name', )
    # return df.to_json(orient='records')


df = pd.read_excel(r'C:\Users\Денис\Downloads\transactions_excel.xlsx')
result = reading_a_file(df)
print(result.head(3))
