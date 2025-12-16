from serialize import students_from_json, students_to_json

# 1. Загружаем студентов из input файла
students = students_from_json("../data/lab_08/students_input.json")

# 2. Выводим на экран
for s in students:
    print(s)

# 3. Сохраняем в output файл
students_to_json(students, "../data/lab_08/students_output.json")
print("\nФайл students_output.json успешно создан!")