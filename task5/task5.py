import numpy as np
import json
from collections.abc import Sequence


# Рекурсивно разворачивает вложенные последовательности
def expand_sequence(seq):
    expanded = []
    for item in seq:
        if isinstance(item, Sequence) and not isinstance(item, str):
            expanded.extend(expand_sequence(item))
        else:
            expanded.append(item)
    return expanded


# Строит матрицу связей для массива
def create_link_matrix(data):
    expanded_data = expand_sequence(data)
    matrix_size = len(expanded_data)
    link_matrix = np.zeros((matrix_size, matrix_size), dtype=int)

    for i, val in enumerate(expanded_data):
        index = int(val) - 1
        for j in range(i + 1):
            link_matrix[int(expanded_data[j]) - 1, index] = 1

    for subgroup in data:
        if isinstance(subgroup, Sequence) and not isinstance(subgroup, str):
            for val in subgroup:
                index = int(val) - 1
                for other_val in subgroup:
                    link_matrix[index, int(other_val) - 1] = 1
                    link_matrix[int(other_val) - 1, index] = 1

    return link_matrix


# Вычисляет основу связей между двумя матрицами
def calculate_basis(matrix1, matrix2):
    transposed_matrix1 = matrix1.T
    transposed_matrix2 = matrix2.T

    combined_relation = np.logical_or(np.multiply(matrix1, matrix2),
                                      np.multiply(transposed_matrix1, transposed_matrix2))

    basis = []
    for i in range(len(combined_relation)):
        for j in range(i, len(combined_relation[i])):
            if not combined_relation[i][j]:
                basis.append([str(i + 1), str(j + 1)])

    return basis


# Преобразует JSON-строку в объект
def parse_json(input_str):
    return json.loads(input_str)


# Основная функция задачи
def task(json_str1, json_str2):
    data1 = parse_json(json_str1)
    data2 = parse_json(json_str2)

    matrix1 = create_link_matrix(data1)
    matrix2 = create_link_matrix(data2)

    return calculate_basis(matrix1, matrix2)


