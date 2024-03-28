'''
how many days was the temp below zero celcius
{number of temperatures collected}
{{temperatures}}
'''
import sys

input_lines = sys.stdin.readlines()
n = int(input_lines[0])
temps = list(map(int, input_lines[1].split()))

count = 0
for temp in temps:
    if temp < 0:
        count += 1

print(count)