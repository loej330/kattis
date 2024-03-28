from sys import stdin; from math import sqrt
o = [ list(map(int, line.split())) for line in stdin.readlines() ]
m = [ o[1] for o in sorted([ (o[i][j], (i, j)) for j in range(3) for i in range(3) ]) ]
l = 0.0; s = {}
for i in range(8):
    d = tuple([ abs(m[i][0] - m[i+1][0]), abs(m[i][1] - m[i+1][1]) ])
    if d not in s: s[d] = (sorted(d)[1] if 0 in d else sqrt((d[0] ** 2) + (d[1] ** 2)))
    l += s[d]
print(l)