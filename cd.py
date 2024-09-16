while (c := input()) != '0 0':
    jack, jill = [{int(input()) for _ in range(n)} for n in map(int, c.split())]
    print(len(jack & jill))
