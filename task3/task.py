import csv
import numpy as np

def task(var: str) -> str:
    h = 0
    readr = csv.reader(var.split("\n"))
    reader = list(readr)
    n = len(reader)
    for i in range(n):
        hj = 0
        for j in range(n):
            for k in range(len(reader[j])):
                hj += ((float(reader[j][k])/n-1)*np.log2((float(reader[j][k])/n-1)))

        h += hj
    return h


if __name__ == "__main__":
    task("0 1\n3 1\n1 0\n1 0\n1 0")
