from typing import Any
import requests


def return_amount_trans(transactions: Any, cur) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях
    """
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]['currency']['code']
    if currency == 'RUB':
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur}&from={currency}&amount={amount}"
        headers = {
            "apikey": "AJ57MO1ENPdazTOcBs3DFXxSxN2kegOK"
        }
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        print(f"Статус код: {status_code}")
        return response.json()['result']


if __name__ == '__main__':
    r = (return_amount_trans(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }
        }, 'RUB'))
    print(r)
