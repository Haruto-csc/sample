S = input()
N = int(input())
p = list(input().split())
eat = ''

for i in p:
    eat += ' '
    eat += ('a' * int(i))

print(S + eat)
