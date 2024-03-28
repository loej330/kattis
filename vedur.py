import sys

input_lines = sys.stdin.readlines()
# v = int(input_lines[0])
# n = int(input_lines[1])
v = int(input_lines[0])
n = int(input_lines[1])

roads = []
for i in range(2, 2+n):
    roads.append(input_lines[i].split())

# print(v, n)
print(roads)