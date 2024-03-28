from sys import stdin
bills = {}; hours = {}; days = 1
for line in stdin.readlines():
    line = line.split(); event = line[0]
    if event == "ENTER":
        name, hour = line[1], int(line[2])
        hours[name] = hour
    elif event == "EXIT":
        name, hour = line[1], int(line[2])
        if name in bills: bills[name] += ((hour - hours[name]) * 0.10)
        else: bills[name] = ((hour - hours[name]) * 0.10)
    elif event == "CLOSE":
        print("Day", days)
        for name, cost in sorted(bills.items()): 
            print(name, "${:.2f}".format(cost))
        print()
        bills = {}; hours = {}; days += 1