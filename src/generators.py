def filter_by_currency(data: list[dict], currency_code: str) -> iter:
    """функция фильтрует транзакции по валюте"""
    for transaction in data:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(data: list[dict]) -> iter:
    """функция возвращает описание транзакции"""
    for transaction in data:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> iter:
    """функция генерирует номер карты"""
    if not 1 <= start + 1 <= 9999_9999_9999_9999:
        raise ValueError("start должен быть от 1 до 9999999999999999")
    if not start < stop <= 9999_9999_9999_9999:
        raise ValueError("stop должен быть больше start и не больше 9999999999999999")

        # Генерируем номера
    for number in range(start, stop + 1):
        # Форматируем число в строку с ведущими нулями
        formatted = str(number).zfill(16)
        # Разбиваем на группы по 4 цифры
        yield " ".join(formatted[i : i + 4] for i in range(0, 16, 4))
