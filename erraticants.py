from collections import OrderedDict

convert = { 'N': (-1, 0), 'E': (0, -1), 'S': (1, 0), 'W': (0, 1) }
add = lambda loc, dir: (loc[0] + dir[0], loc[1] + dir[1])

for _ in range(int(input())):
    input()
    steps = int(input())
    dirs = [ input() for _ in range(steps) ]

    if steps == 0:  print(0); continue
    start = ant = (0, 0)
    coords = [ant] + [ ant := add(ant, convert[dir]) for dir in dirs ]
    end = coords[-1]
    graph = { coord: set() for coord in coords }
    for i in range(1, len(coords)-1): 
        graph[coords[i]].update({coords[i-1], coords[i+1]})
    graph[start].add(coords[1])
    graph[end].add(coords[-1])

    unvisited = OrderedDict({start:0})
    visited = set() 
    while len(unvisited) > 0:
        node, depth = unvisited.popitem(last=False)
        if node == end: print(depth); break
        for next in graph[node]:
            if next not in visited: unvisited[next] = depth + 1
        visited.add(node)