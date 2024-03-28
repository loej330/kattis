while (n:=int(input())) != 0:
    x,y = zip(*[map(int, input().split()) for _ in range(n)])
    t = sum(x[i]*y[j]-x[j]*y[i] for i,j in zip(range(n),list(range(1,n))+[0]))/2
    print(f"CCW {t}" if t >= 0 else f"CW {-t}")