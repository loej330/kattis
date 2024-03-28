from sys import stdin; lines = stdin.readlines()

def score(a, b):
    if (a == 1 and b == 2) or (a == 2 and b == 1): return 1000
    elif (a == b): return a * 100
    else: return (max(a, b) * 10) + min(a, b)

for line in lines[:-1]:
    [s0, s1, r0, r1] = map(int, line.split())
    s = score(s0, s1)
    r = score(r0, r1)
    if s > r: print("Player 1 wins.")
    elif r > s: print("Player 2 wins.")
    else: print("Tie.")
