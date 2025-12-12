import argparse
import os
import sys
sys.path.append('/Users/mda/Desktop/python_labs/src/lab05/')
from json_csv import json_to_csv
from json_csv import csv_to_json
from csv_xlsx import csv_to_xlsx

def json2csv(input_file, output_file):
    json_to_csv(input_file, output_file)

def csv2json(input_file, output_file):
    csv_to_json(input_file, output_file)

def csv2xlsx(input_file, output_file):
    csv_to_xlsx(input_file, output_file)

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # json2csv
    p1 = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    # csv2json
    p2 = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    # csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    # Проверяем, существует ли входной файл
    if not os.path.exists(args.input):
        print(f"Ошибка: файл {args.input} не найден", file=sys.stderr)
        sys.exit(1)

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        print("Готово!")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()