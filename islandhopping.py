from itertools import combinations
from math import dist

n_graphs = int(input())
for k_graph in range(n_graphs):
    n_nodes = int(input()); visited = {}; tot_dist = 0
    graph = { tuple(map(float, input().split())) for _ in range(n_nodes) }
    edges = sorted([ (dist(a, b), a, b) for [a, b] in combinations(graph, 2) ])
    for edge in edges:
        if len(graph) == len(visited): break