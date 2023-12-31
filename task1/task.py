import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='путь к файлу CSV')
parser.add_argument('row', type=int, help='номер строки')
parser.add_argument('col', type=int, help='номер столбца')
args = parser.parse_args()

with open(args.file, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

value = data[args.row][args.col]
print(value)