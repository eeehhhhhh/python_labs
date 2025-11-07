from typing import Iterable, Sequence
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str: #изменить кодировку: encoding="cp1251"
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_len}")
    
    # Проверка что заголовок соответствует длине строк
    if header and len(header) != len(rows[0]):
        raise ValueError(f"Заголовок имеет длину {len(header)}, а строки - {len(rows[0])}")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        w.writerows(rows)
from io_txt_csv import read_text, write_csv
txt = read_text("data/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV