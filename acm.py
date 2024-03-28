from sys import stdin; lines = stdin.readlines()
from collections import defaultdict

problems = defaultdict(lambda: [0, 0]) 

for line in lines[:-1]:
    [ time, problem, valid ] = line.split()
    time = int(time)
    if valid == 'right':
        problems[problem][0] += time 
        problems[problem][1] = 1
    else:
        problems[problem][0] += 20

total = 0
score = 0
for key, val in problems.items():
    if val[1] == 1:
        total += 1
        score += val[0]

print(total, score)