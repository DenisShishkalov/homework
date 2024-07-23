from typing import Any


def mask_account_card(number: Any) -> str:
    """Функция принимает номер карты или номер счета
    :rtype: object
    """
    name_card = ""

    if "Счет " in number or "Счёт " in number:
        return f"Счет **{number[-4:]}"
    else:
        for i in number:
            if i.isalpha():
                name_card += i

        return f"{name_card} {number[-16: -12]} {number[-11:-9]}** **** {number[-4:]}"


# mask_account_card(number="Счет 12246578657898764356")
# mask_account_card(number="Visa 1245123412341234")


def get_data(data: Any) -> str:
    """Функция преобразования даты"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"


# get_data(data="2018-07-11T02:26:18.671407")
