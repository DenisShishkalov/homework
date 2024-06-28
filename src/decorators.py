from functools import wraps
from typing import Callable, Any


def log(filename: str) -> Callable:
    def decorator(func: Any):
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
             try:
                if filename:
                    result = func(*args, **kwargs)
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write('\nmy_function ok')
                else:
                    print("\nmy_function ok")

             except Exception as f:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'my_function error: {f} Inputs: {args}, {kwargs}')
             return result
        return inner
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """ Функция, складывающая 2 числа"""
    return x + y

my_function(1, 2)