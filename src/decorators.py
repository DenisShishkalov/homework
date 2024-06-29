from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """ Декоратор, логирующий вызов функции и ее результат в файл или консоль
    :param filename: путь к файлу для записи логов. Если не указан, логи выводятся в консоль
    :return: Обертка функции, которая логирует вызов и ее результат
    """
    def decorator(func: Any) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Callable:
            try:
                if filename:
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("\nmy_function ok")

                else:
                    print("\nmy_function ok")

            except Exception as e:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"\nmy_function error: {e} Inputs: {args}, {kwargs}")
                raise Exception(f"Ошибка: {e}")
            return result

        return inner

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция, складывающая 2 числа"""
    return x + y


print(my_function(1, 2))
# print(my_function(['fdh'], 'gfh'))
