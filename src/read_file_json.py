import json
from typing import Any

from config import ROOT_DIR


def read_json_file() -> Any:
    """Функция чтения файл json."""
    with open(ROOT_DIR + "/data/products.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
