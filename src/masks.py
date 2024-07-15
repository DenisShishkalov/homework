import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(r"C:\Users\Денис\PycharmProjects\01\logs\masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_account(number: str) -> str:
    """Функция, маскирующая номер счета или карты"""
    try:
        logger.info("Проверяем корректность полученных данных и маскируем их")
        if str(number).isdigit() and len(number) == 16:
            return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
        elif str(number).isdigit() and len(number) == 20:
            return f"**{number[-4::]}"
        else:
            logger.info("Выводим сообщение, что данные некорректны")
            return "Введены некорректные данные"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


# print(get_mask_account(number="3234123412341234"))
# print(get_mask_account(number="53125674431399887757"))
print(get_mask_account(number="fdgswe4252312653467547"))
