from math import log2

def calculate_entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p > 0)

def task():
    total_outcomes = 36

    probabilities_A = {i:0 for i in range(2, 13)}
    for i in range(1, 7):
        for j in range(1, 7):
            probabilities_A[i+j] += 1
    probabilities_A = [count / total_outcomes for count in probabilities_A.values()]

    probabilities_B = {i:0 for i in range(1, 37)}
    for i in range(1, 7):
        for j in range(1, 7):
            probabilities_B[i*j] += 1
    probabilities_B = [count / total_outcomes for count in probabilities_B.values()]

    joint_probabilities = {}
    for i in range(1, 7):
        for j in range(1, 7):
            joint_key = (i+j, i*j)
            joint_probabilities[joint_key] = joint_probabilities.get(joint_key, 0) + 1/total_outcomes

    H_A = calculate_entropy(probabilities_A)
    H_B = calculate_entropy(probabilities_B)
    H_AB = calculate_entropy(joint_probabilities.values())
    Ha_B = H_AB - H_A
    I_A_B = H_B - Ha_B

    return [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(Ha_B, 2), round(I_A_B, 2)]
