[ n, t ] = list(map(int, input().split()))
nums = list(map(int, input().split()))
count = 0; total = 0
for num in nums:
    total += num
    if total > t: break
    count += 1
print(count)