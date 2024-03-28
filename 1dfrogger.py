def game():
    ints = lambda: list(map(int, input().split()))
    n, s, m = ints()
    board = ints()

    s = s - 1
    past = set() 
    i = 0 

    while True:
        if s < 0: return ('left', str(i))
        elif s >= n: return ('right', str(i))
        elif s in past: return ('cycle', str(i))
        elif (number := board[s]) == m: return ('magic', str(i))

        past.add(s)
        s += number
        i += 1

print('\n'.join(game()))
