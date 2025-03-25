def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED'):
    """функция принимающая список словарей и возвращающая отфильтрованный список словарей"""
    new_list_dict = []
    for d in list_dict:
        if d["state"] == state:
            new_list_dict.append(d)
    return new_list_dict



def sort_by_date(list_dict: list[dict], parameter: bool = True):
    """функиия принимает список словарей и сортирует по дате"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=parameter)

