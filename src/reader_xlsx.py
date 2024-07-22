import pandas as pd
from config import file_transaction_xlsx


def reading_a_file(df: pd.DataFrame) -> list[dict]:
    """
    Функция считывания информации из xlsx файла
    """
    # return df.sort_values(by='currency_name')
    return df.to_dict(orient="records")


path = file_transaction_xlsx
ret = pd.read_excel(path)

reading_a_file(ret)
# print(reading_a_file(ret))
