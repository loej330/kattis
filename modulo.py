import sys

numbers = list(map(int, sys.stdin.readlines()))
 
for number in numbers:
    count += (number % 42)

print(input_lines)