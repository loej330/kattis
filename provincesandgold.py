import sys

v_worth = [6, 3, 1]
t_worth = [3, 2, 1]

counts = list(map(int, sys.stdin.readlines()[0].split()))
total = [ t_worth[i] * counts[i] for i in range(3) ]

if total >= 8: print("Province or Gold")
elif total >= 6: print("Duchy or Gold")
elif total >= 5: print("Duchy or Silver")
elif total >= 3: print("Estate or Silver")
elif total >= 2: print("Estate or Copper")
else: print("Copper")