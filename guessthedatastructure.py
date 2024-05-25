from collections import deque
from bisect import insort

ri = lambda a,b: a.append(b)
si = lambda a,b: insort(a,b,key=lambda x: -x)
rp = lambda a: a.pop()
lp = lambda a: a.popleft()
ds = [ (ri, lp, 'queue', ), (ri, rp, 'stack'), (si, lp, 'priority queue')] 

while True:
    try:
        dd = [(i, deque()) for i in range(3)]
        for _ in range(int(input())):
            o, v = map(int, input().split())
            if o == 1:
                for d in dd: ds[d[0]][0](d[1], v)
            else: dd = [ d for d in dd if d[1] and ds[d[0]][1](d[1]) == v ]
        if len(dd) > 1: print('not sure')
        elif len(dd) == 1: print(ds[dd[0][0]][2])
        else: print('impossible')
    except EOFError: break
