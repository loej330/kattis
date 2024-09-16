types = { '0': 'binary', '1': 'decimal' } 
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

r, c = map(int, input().split())
grid = tuple(input().strip() for _ in range(r))
n = int(input())
zones = [[ 0 for _ in range(c) ] for _ in range(r)]
zone_id = 0

for i in range(r):
    for j in range(c):
        if zones[i][j] != 0: continue
        zone_id += 1
        zone_type = grid[i][j]
        points = [(i, j)]
        while points:
            n_points = []
            for point in points:
                for move in moves:
                    ik = point[0] + move[0]
                    jk = point[1] + move[1]
                    if (
                        (ik < 0 or ik >= r) or
                        (jk < 0 or jk >= c) or
                        (grid[ik][jk] != zone_type) or
                        (zones[ik][jk] == zone_id)
                    ): continue
                    zones[ik][jk] = zone_id
                    n_points += [(ik, jk)]
            points = n_points

for _ in range(n):
    r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())
    if zones[r1][c1] == zones[r2][c2]: print(types[grid[r1][c1]])
    else: print('neither')
