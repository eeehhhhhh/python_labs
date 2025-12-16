import sys
from group import Group
sys.path.append('/Users/mda/Desktop/python_labs/src/lab_08/')
from models import Student
group = Group("/Users/mda/Desktop/python_labs/data/lab_09/students.csv")

print("=== 1. Добавление студентов ===")
group.add(Student("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3))
group.add(Student("Петров Петр", "2004-05-15", "ПИ-22-2", 4.7))
group.add(Student("Сидорова Анна", "2003-12-22", "БИВТ-21-1", 3.9))
print("Добавлено 3 студента\n")

print("=== 2. Список всех студентов ===")
all_students = group.list()
if all_students:
    for s in all_students:
        print(f"  - {s}")
else:
    print("  Нет студентов")
print()

print("=== 3. Поиск по подстроке 'ив' ===")
found = group.find("ив")
if found:
    for s in found:
        print(f"  - {s}")
else:
    print("  Не найдено")
print()

print("=== 4. Обновление студента ===")
if group.update("Иванов Иван", gpa=4.8, group="БИВТ-21-2"):
    print("  Студент обновлен")
else:
    print("  Студент не найден")
print()

print("=== 5. Удаление студента ===")
if group.remove("Петров Петр"):
    print("  Студент удален")
else:
    print("  Студент не найден")
print()

print("=== 6. Финальный список ===")
final_students = group.list()
if final_students:
    for s in final_students:
        print(f"  - {s}")
else:
    print("  Нет студентов")