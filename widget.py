


def mask_account_card(number: str) -> str:
    """ Функция принимает номер карты или номер счета"""
    name_card = ''
    # full_number = list(number).remove(number_card)
    if "Счет " in number or "Счёт " in number:
        # return get_mask_account(number)
        return f"Счет **{number[-4:]}"
    else:
        for i in number:
            if i.isalpha():
                name_card += i
        return f"{name_card} {n[: 4]} {name_card[4:6]}** **** {name_card[12:16]}"

print(mask_account_card(number="Счет 12246578657898764356"))
print(mask_account_card(number= "Visa jgkghj 1245123412341234"))
