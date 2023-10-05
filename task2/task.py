import csv
from collections import defaultdict

def task(var: str) -> str:
    reader = csv.reader(var.split("\n"))
    graph = defaultdict(set)
    for row in reader:
        if len(row) == 2:
            graph[row[0]].add(row[1])

    relations = set(graph.keys()) | set.union(*graph.values())
    ext_lens = defaultdict(dict)

    for node in graph.keys():
        for rel in relations:
            ext_lens[node][rel] = 1 if rel in graph[node] else 0

    for node in graph.keys():
        for rel in relations:
            if ext_lens[node][rel] == 1:
                for parent in graph.keys():
                    if node in graph[parent]:
                        ext_lens[parent][rel] += 1

    result = []
    for node in sorted(graph.keys()):
        result.append(",".join(str(ext_lens[node][rel]) for rel in sorted(relations)))

    return "\n".join(result)
