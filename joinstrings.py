N = int(input())
if N == 1: print(input())
else:
    S = [""] + [input().strip() for _ in range(N)]
    ops = [tuple(map(int, input().split())) for _ in range(N-1)]
    nums = [ i for i in range(N+1) ]
    for a, b in ops: nums[a] = (nums[a], nums[b])

    def output(tree):
        for node in tree:
            if isinstance(node, tuple): output(node)
            else: print(S[node], end='')
    output(nums[ops[-1][0]])
    print()
