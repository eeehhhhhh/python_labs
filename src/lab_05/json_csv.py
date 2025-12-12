import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    with open(json_path, 'r', encoding='utf-8') as jf:
        try:
            data = json.load(jf)
        except json.JSONDecodeError:
            raise ValueError("Файл не является валидным JSON")

    if not isinstance(data, list):
        raise ValueError("JSON должен быть списком объектов")
    if len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы в списке должны быть словарями")

    fieldnames = list(data[0].keys())
    for item in data[1:]:
        for key in item.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            for key in fieldnames:
                row.setdefault(key, '')
            writer.writerow(row)

def csv_to_json(csv_path: str, json_path: str) -> None:

    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    with open(csv_path, 'r', encoding='utf-8') as cf:
        reader = csv.DictReader(cf)
        if reader.fieldnames is None:
            raise ValueError("CSV файл пуст или не содержит заголовка")
        data = list(reader)

    if len(data) == 0:
        raise ValueError("CSV файл пуст")

    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)