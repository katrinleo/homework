def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """функция принимающая список словарей и
    возвращающая отфильтрованный список словарей"""
    output_data = []
    for d in data:
        if d["state"] == state:
            output_data.append(d)
    return output_data


def sort_by_date(data: list[dict], bool_parameter: bool = True) -> list[dict]:
    """функиия принимает список словарей и сортирует по дате"""
    return sorted(data, key=lambda x: x["date"], reverse=bool_parameter)
