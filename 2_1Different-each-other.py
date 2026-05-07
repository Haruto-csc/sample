n = int(input())
a = list(input().split())

ans = 'YES'
for i in range(n):
    for j in range(n):
        if (i == j):
            continue
        elif (a[i] == a[j]):
            ans = 'NO'
            break

print(ans)
