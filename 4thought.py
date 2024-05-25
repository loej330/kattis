# make every possible number generated - only 64!
# remove any solution that yields the same number
# use this info to construct a large dictionary 
# possible solutions is deterministic

# code used to generate the solutions
# symbs = [ '*', '+', '-', '/' ]
# ops = [ '*', '+', '-', '//' ]
# solutions = {}
# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             result = (eval(f"4{ops[i]}4{ops[j]}4{ops[k]}4"))
#             if result not in solutions:
#                 solutions[result] = f"{symbs[i]}{symbs[j]}{symbs[k]}"
# print(solutions)

s = {256: '***', 68: '**+', 60: '**-', 16: '**/', 32: '*+*', 24: '*++', 17: '*+/', 0: '*-*', 8: '*--', 15: '*-/', 1: '*//', 9: '++/', -8: '+-*', 7: '+-/', 4: '+//', -60: '-**', -16: '-*-', -1: '--/', 2: '/+/', -15: '/-*', -7: '/--', -4: '//-'}

for _ in range(int(input())):
    x = int(input())
    if x in s: 
        a, b, c = s[x]
        print(f"4 {a} 4 {b} 4 {c} 4 = {x}")
    else: print("no solution")
