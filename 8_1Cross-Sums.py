N = int(input())
A = []
total = 0
for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    total += A[i][i]
    total += A[N - 1 - i][N - 1 - i]
if N % 2 == 1:
    total -= A[N // 2][N // 2]

print(total)
