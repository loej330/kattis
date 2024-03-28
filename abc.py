import sys
order = {'A': 0, 'B': 1, 'C': 2}
prob_input = sys.stdin.readlines()

numbers = sorted(prob_input[0].split())
letters = prob_input[1].strip()

for letter in letters:
    print(numbers[order[letter]], end=' ')
