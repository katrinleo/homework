import json
import os


def load_json_list(path_to_file: str) -> list[dict | None]:
    """загружает список финансовых транзакци из JSON - файла"""
    if not os.path.exists(path_to_file) or os.path.getsize(path_to_file) == 0:
        return []
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []
