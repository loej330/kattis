import sys
moves = sys.stdin.readlines()[0].strip()
cups = [1, 0 , 0]

lambda A = (): [cups[1]] + [cups[0]] + [cups[2]]
lambda B = (): [cups[0]] + [cups[2]] + [cups[1]]
lambda C = (): [cups[2]] + [cups[1]] + [cups[0]]

for move in moves:
    cups = eval(f"{move}()")
print(cups.index(1))