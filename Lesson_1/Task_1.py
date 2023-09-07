import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file", help="путь к файлу csv")
parser.add_argument("row", type=int, help="номер строки")
parser.add_argument("column", type=int, help="номер столбца")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == args.row - 1:
            print(row[args.column - 1])
            break