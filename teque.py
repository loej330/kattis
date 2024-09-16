from dataclasses import dataclass
@dataclass
class Node:
    value: int
    next: int = -1
    prev: int = -1

teque = dict() 
head = tail = middle = new = 0
odd = True
N = int(input())
teque[new] = Node(value=int(input().split()[1]))

for _ in range(N-1):
    S, x = input().split()
    x = int(x)
    if S[0] == 'p':
        new += 1
        odd = not odd
        teque[new] = Node(value=x)
        match S[5]:
            case 'f':
                teque[new].next = head
                teque[head].prev = new
                head = new
                if odd: middle = teque[middle].prev
            case 'b':
                teque[new].prev = tail
                teque[tail].next = new
                tail = new
                if not odd: middle = teque[middle].next
            case 'm':
                if odd:
                    teque[new].next = middle
                    teque[new].prev = teque[middle].prev
                    teque[teque[middle].prev].next = new
                    teque[middle].prev = new
                else:
                    teque[new].next = teque[middle].next
                    teque[new].prev = middle
                    teque[teque[middle].next].prev = new
                    teque[middle].next = new
                middle = new
    else:
        current = head
        for _ in range(x):
            current = teque[current].next
        print(teque[current].value) 
