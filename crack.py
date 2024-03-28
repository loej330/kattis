from collections import deque; e=enumerate; t=tuple
p = lambda s,y,x: t(t((v+1)%4 if i==x or j==y else v for j,v in e(r))for i,r in e(s))
def crack():
    b = t(t(map(int,input().split())) for _ in range(3)); v = {b:0}; q = deque([b])
    while q:
        c = q.popleft()
        for y,x in map(lambda i: (i//3, i%3), range(9)):
            k = p(c, y, x); 
            if sum(map(sum, k)) == 0: return v[c] + 1
            if k not in v: v[k] = v[c] + 1; q.append(k)
    return -1
print(crack())