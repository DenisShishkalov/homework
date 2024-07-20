from typing import Any

import pandas as pd


def reading_a_file(df: pd.DataFrame) -> Any:
    """
    Функция считывания информации из xlsx файла
    """
    # return df.sort_values(by='currency_name')
    return df.to_dict(orient="records")


df = pd.read_excel(r"C:\Users\Денис\Downloads\transactions_excel.xlsx")
result = reading_a_file(df)
print(type(result))
print(result)
