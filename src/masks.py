def get_mask_account(number: str) -> str:
    """Функция, маскирующая номер счета или карты"""

    if str(number) == "":
        raise AssertionError

    # if str(number).isalpha() or len(number) != 16:
    #     raise ValueError('Ошибка')
    elif str(number).isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    elif str(number).isdigit() and len(number) == 20:
        return f"**{number[-4::]}"
    else:
        # pass
        raise ValueError("Введены некоректные данные")


# print(get_mask_account(number="3234123412341234"))
# print(get_mask_account(number="53125674431399887757"))
# print(get_mask_account(number="fdgswe4252312653467547"))
