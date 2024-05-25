from collections import Counter

# simplicity == how many unique letters
def main():
    letter_counts = Counter(input()).most_common()
    if len(letter_counts) <= 2: return 0
    return sum(count[1] for count in letter_counts[2:])
print(main())

