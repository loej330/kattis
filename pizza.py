import math

for _ in range(int(input())):
    r, n, degrees, minutes, seconds = map(int, input().split())
    theta = degrees + (minutes / 60) + (seconds / 3600)
    cuts = [ ]; marker = 0.0
    for _ in range(n):
        cuts += [ marker ]
        marker = (marker + theta) % 360
        if marker in cuts: break
    cuts = sorted(cuts) + [ 360.0 ]
    largest = max( abs(cuts[i] - cuts[i+1]) for i in range(len(cuts) - 1))
    print((largest / 360) * math.pi * (r ** 2))