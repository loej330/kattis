from sys import stdin; lines = stdin.readlines()
weights = sorted([ int(l.strip()) for l in lines[1:] ])
sums = { 0 : True }; c_sum = 1000000; b_sum = 0
for weight in weights:
    i_sums = list(reversed(sorted(sums.keys())))
    for i_sum in i_sums: sums[i_sum + weight] = True
for i_sum in reversed(sorted(sums.keys())):
    t_sum = abs(i_sum - 1000)
    if t_sum < c_sum: c_sum = t_sum; b_sum = i_sum
    elif t_sum == c_sum: break
print(b_sum)