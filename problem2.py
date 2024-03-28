def func():
    stack = []
    start = { '(', '[', '{' }
    match = { ')':'(', ']':'[', '}':'{' }
    for i, c in zip(range(int(input())),(input().strip())):
        if c == ' ': continue
        if c in start: stack.append(c); continue
        if len(stack) == 0 or match[c] != stack[-1]: print(c, i); return
        stack.pop()
    print("ok so far")
func()