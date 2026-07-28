"""
Robot Memory
"""

import os
import json
from datetime import datetime

from config import MEMORY_FILE, MAX_MEMORY_LINES


def _load():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:

        return []


def _save(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def add(role, text):

    data = _load()

    data.append({

        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "role": role,

        "text": text

    })

    if len(data) > MAX_MEMORY_LINES:

        data = data[-MAX_MEMORY_LINES:]

    _save(data)


def history():

    return _load()


def clear():

    _save([])


def last(count=10):

    data = _load()

    return data[-count:]


def search(keyword):

    result = []

    for item in _load():

        if keyword.lower() in item["text"].lower():

            result.append(item)

    return result


def export_text():

    text = ""

    for item in _load():

        text += (
            f"[{item['time']}] "
            f"{item['role']}: "
            f"{item['text']}\n"
        )

    return text
