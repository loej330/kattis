last = input()
animals = [ input() for _ in range(int(input())) ]

def doit():
    potential = -1
    for i, choice in enumerate(animals):
        if last[-1] == choice[0]:
            perfect = True
            for next in animals[:i] + animals[i+1:] + [ last ]:
                if choice[-1] == next[0]: 
                    potential = i 
                    perfect = False
                    break
            if perfect == True: return(f"{choice}!")
    if potential > -1: return animals[potential]
    else: return '?'

print(doit())
