from sys import stdin; lines = stdin.readlines()
[X, Y, N] = map(int, lines[0].split())
for i in range(1, N + 1):
    fizz = i % X == 0; buzz = i % Y == 0
    if fizz and buzz: print('FizzBuzz')
    elif fizz: print('Fizz')
    elif buzz: print('Buzz')
    else: print(i)