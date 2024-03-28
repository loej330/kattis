import sys
import math

import sys


[X, Y] = list(map(int, sys.stdin.readline().split()))


if Y == 1:
    if X == 0: print("ALL GOOD")
    else: print("IMPOSSIBLE")
elif Y == -1: print("ALL GOOD")
else:
    Z = (-X / (Y - 1))
    if len((str(float(Z))).split('.')[1]) <= 6 : print(Z)
    else : print("IMPOSSIBLE")