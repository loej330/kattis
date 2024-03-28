from sys import stdin; lines = stdin.readlines()
intline = lambda i : list(map(int, lines[i].split()))

[ nb, nn, ne ] = intline(0)
[ b, n, e ] = intline(1)
kayaks = sorted(intline(2)) 

#v = c(s + s)
# do we want the weakest swimmers with the strongest speed kayaks?

