import sys
import csv
from pathlib import Path
sys.path.append('/Users/mda/Desktop/python_labs/src/lab08/')
from models import Student
class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        #Создаёт файл с заголовком, если его нет
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()

    def _read_all(self):
        #Читает все строки из CSV и возвращает список словарей
        rows = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(row)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        return rows

    def list(self):
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                # Преобразуем gpa из строки в float
                student_dict = {
                    'fio': row['fio'],
                    'birthdate': row['birthdate'],
                    'group': row['group'],
                    'gpa': float(row['gpa'])
                }
                students.append(Student.from_dict(student_dict))
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании студента {row.get('fio', 'Unknown')}: {e}")
                continue
        return students

    def add(self, student: Student):
        try:
            with open(self.path, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writerow(student.to_dict())
            return True
        except Exception as e:
            print(f"Ошибка при добавлении студента: {e}")
            return False

    def find(self, substr: str):
        rows = self._read_all()
        result = []
        for row in rows:
            try:
                if substr.lower() in row['fio'].lower():
                    student_dict = {
                        'fio': row['fio'],
                        'birthdate': row['birthdate'],
                        'group': row['group'],
                        'gpa': float(row['gpa'])
                    }
                    result.append(Student.from_dict(student_dict))
            except (ValueError, KeyError) as e:
                print(f"Ошибка при обработке студента {row.get('fio', 'Unknown')}: {e}")
                continue
        return result

    def remove(self, fio: str):
        rows = self._read_all()
        if not rows:
            return False
            
        new_rows = [row for row in rows if row['fio'] != fio]
        
        if len(new_rows) == len(rows):
            return False  # Не нашли студента
        
        try:
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
                writer.writerows(new_rows)
            return True
        except Exception as e:
            print(f"Ошибка при удалении студента: {e}")
            return False

    def update(self, fio: str, **fields):
        rows = self._read_all()
        if not rows:
            return False
            
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for key, value in fields.items():
                    if key in row:
                        # Преобразуем gpa к строке, если это число
                        if key == 'gpa' and isinstance(value, (int, float)):
                            row[key] = str(value)
                        else:
                            row[key] = value
                updated = True
                break
        
        if updated:
            try:
                with open(self.path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                    writer.writeheader()
                    writer.writerows(rows)
                return True
            except Exception as e:
                print(f"Ошибка при обновлении студента: {e}")
                return False
        return False