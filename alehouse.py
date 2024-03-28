from sys import stdin; lines = stdin.readlines()

[ num_people, visit_time ] = map(int, lines[0].split())

times = {}
for line in lines[1:]:
    [start, end] = map(int, line.split())
    start = (max(0, start - visit_time), 0); end = (end, 1)
    for time in [start, end]:
        times[time] = (times[time] + 1 if time in times else 1)

max_people = 0
stack = 0
for time, count in sorted(times.items()):
    if time[1] == 0: stack += count
    else: stack -= count
    max_people = max(max_people, stack)

print(max_people)