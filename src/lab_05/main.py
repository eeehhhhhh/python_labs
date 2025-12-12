from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

# Тест JSON → CSV
print("Конвертация JSON → CSV...")
json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
print("Готово: data/out/people_from_json.csv")

# Тест CSV → JSON
print("Конвертация CSV → JSON...")
csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
print("Готово: data/out/people_from_csv.json")

# Тест CSV → XLSX
print("Конвертация CSV → XLSX...")
csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
print("Готово: data/out/cities.xlsx")