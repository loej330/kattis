prime = lambda x: not any (x % i == 0 for i in range(2, x))
while (n:=int(input())):
    n2 = n * 2
    while not prime(n2): n2 += 1
    print(f'{n2}' if prime(n) else f'{n2} ({n} is not prime)')