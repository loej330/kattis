from sys import stdin; from itertools import combinations; from math import sqrt 
p = [ tuple(map(int, line.split())) for line in stdin.readlines() ]
# t = list(combinations(p, 2))
d = [ (abs(x2-x1), abs(y2-y1)) for [x1,y1],[x2,y2] in combinations(p, 2) ]
# print(t)
# print(d)

