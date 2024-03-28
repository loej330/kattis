import sys
import math

for i in sys.stdin:
    n = int(i.split()[0])

print(math.ceil(math.log2(n)) + 1 )