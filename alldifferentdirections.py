import math as m
while (n:=int(input())) != 0:
    xs, ys = [], []
    for _ in range(n):
        x, y, _, a, *s = input().split()
        x, y, a = float(x), float(y), m.radians(float(a))
        for i in range(0, len(s), 2): 
            if s[i] == 'turn': a += m.radians(float(s[i+1]))
            else: w = float(s[i+1]); x += (m.cos(a) * w); y += (m.sin(a) * w)
        xs += [x]; ys += [y]
    xa = sum(xs) / n; ya = sum(ys) / n
    d = max([ m.dist((xa, ya), (x, y)) for x, y in zip(xs, ys) ])
    print(xa, ya, d)