N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
difference = []
for i in range(N):
    difference.append(A[i] - B[i])

print(*difference, sep = ' ')
