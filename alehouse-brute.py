from sys import stdin; lines = stdin.readlines()

[ num_people, visit_time ] = map(int, lines[0].split())
[ starts, ends ] = list(zip(*[ map(int, line.split()) for line in lines[1:] ]))

schedule = { t: [] for t in [ i for i in range(min(starts), max(starts)+1) ] }
for person in range(len(starts)):
    for time in range(starts[person], ends[person] + 1):
        schedule[time].append(person)

max_people = 0
for start in range(len(schedule)):
    visit = []
    for time in range(start, min(max(ends), start + visit_time) + 1):
        visit += schedule[time]
    max_people = max(max_people, len(set(visit)))
    
print(max_people)
