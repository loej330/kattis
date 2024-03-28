for _ in range(int(input())):
    N = int(input()+input())
    print("YES" if not (sum(int(input()) for i in range(N)) % N) else "NO")