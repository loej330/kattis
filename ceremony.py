from sys import stdin; lines = stdin.readlines()

towers = sorted(list(map(int, lines[1].split())))
charges = 0

while len(towers) > 0:
    if len(towers) > towers[-1]: towers = [ t - 1 for t in towers if t > 1 ]
    else: towers.pop()
    charges += 1

print(charges)