from math import sqrt
[x, y, x1, y1, x2, y2] = map(int, input().split())
ds = (x1-x, x-x2, y1-y, y-y2); p = tuple( 1 if d >= 0 else 0 for d in ds )
if p.count(1) == 1: print(float(ds[p.index(1)]))
else: [w, h] = [ ds[i] for i in range(4) if p[i] ]; print(sqrt(pow(w, 2) + pow(h, 2)))