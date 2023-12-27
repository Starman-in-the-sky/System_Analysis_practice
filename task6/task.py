import json
import numpy as np

def compare_elements(ranking):
    num_experiments = len(ranking)
    num_elements = len(ranking[0])
    comparison_matrices = [np.zeros((num_experiments, num_experiments)) + 0.5 for _ in range(num_elements)]

    for col in range(num_elements):
        for row1 in range(num_experiments):
            for row2 in range(num_experiments):
                if ranking[row1][col] > ranking[row2][col]:
                    comparison_matrices[col][row1][row2] = 1
                elif ranking[row1][col] < ranking[row2][col]:
                    comparison_matrices[col][row1][row2] = 0
    return comparison_matrices

def calculate_preference_matrix(comparisons):
    num_rows = len(comparisons[0])
    num_cols = len(comparisons[0][0])
    num_comparisons = len(comparisons)
    preference_matrix = np.zeros((num_rows, num_cols))

    for row in range(num_rows):
        for col in range(num_cols):
            pref_values = [comparisons[exp][row][col] for exp in range(num_comparisons)]
            preference_matrix[row][col] = np.mean(pref_values)
    return preference_matrix

def compute_estimation(matrix, tolerance):
    num_elements = len(matrix)
    current_vector = np.ones(num_elements) / num_elements
    while True:
        next_vector = matrix @ current_vector
        next_vector /= next_vector.sum()

        if np.max(np.abs(next_vector - current_vector)) <= tolerance:
            break
        current_vector = next_vector

    return np.round(current_vector, 3)

def process_json(json_str):
    return json.loads(json_str)

def task(json_input):
    ranks = np.array(process_json(json_input)).T
    comparison_matrices = compare_elements(ranks)
    preference_matrix = calculate_preference_matrix(comparison_matrices)
    final_scores = compute_estimation(preference_matrix, 0.001)
    return json.dumps(final_scores.tolist())