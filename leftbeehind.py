import sys

# for case in sys.stdin.readlines():
while True:
    next_case = sys.stdin.readline().strip()
    if next_case == '0 0': break
    [x, y] = list(map(int, next_case.split()))
    if x + y == 13: print('Never speak again.')
    elif x - y > 0: print('To the convention.')
    elif x - y < 0: print('Left beehind.')
    else: print('Undecided.')