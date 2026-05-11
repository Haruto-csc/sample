N,M = map(int, input().split())
A = sorted(tuple(map(int, input().split())), reverse=True)
B = tuple(map(int, input().split()))
total = 0
for i in B:
    for j in A:
        if i >= j:
            total += j
            break
print(total)
