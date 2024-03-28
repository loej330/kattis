import sys
for p in sys.stdin.readlines():
    p = p.strip()
    if p == "P=NP": print('skipped'); continue
    if len(p) == 3 and p[1] == '+':
        print(eval(p))