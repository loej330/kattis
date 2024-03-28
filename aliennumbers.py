for case in range(int(input())):
    al, sl, tl = input().split()
    tt = { sl[i]:str(i) for i in range(len(sl)) }
    ss = { i:tl[i] for i in range(len(tl))}
    I = int(''.join(map(tt.get, al)), len(sl))
    S = []
    while I > 0:
        S = [I % len(tl)] + S
        I //= len(tl)
    print(f"Case #{case+1}: {''.join(map(ss.get, S))}")