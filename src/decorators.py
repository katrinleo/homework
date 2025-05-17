import functools
import sys


def log(filename=None):
    """функция-декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки описание транзакции"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"{func.__name__} error: {error_type}. " f"Inputs: {args}, {kwargs}\n"
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    sys.stdout.write(log_message)

        return wrapper

    return decorator
