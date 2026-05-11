N = int(input())
X = list(map(int, input().split()))

for i in range(N):
    X.remove(max(X))
    X.remove(min(X))

print(sum(X) / len(X))
