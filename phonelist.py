def do():  
    prefix = [ set() for _ in range(11) ]
    for num in sorted([ input() for _ in range(int(input()))], reverse=True):
        if num in prefix[len(num)]: return("NO")
        for i in range(len(num)+1):
            prefix_num = num[:i]
            if prefix_num not in prefix[i]: prefix[i].add(prefix_num)
    return("YES")

for _ in range(int(input())):
    print(do())
