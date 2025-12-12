import csv
from openpyxl import Workbook
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертируем CSV в XLSX с помощью openpyxl.
    """
    #Проверяем, существует ли файл
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    with open(csv_path, 'r', encoding='utf-8') as cf:
        reader = csv.reader(cf)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("CSV файл пуст")
        rows = list(reader)

    if len(header) == 0:
        raise ValueError("CSV файл не содержит заголовка")

    #Создаём новую Excel книгу
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    ws.append(header)

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        #Минимальная ширина — 8 символов
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column].width = adjusted_width

    #Сохраняем файл
    wb.save(xlsx_path)