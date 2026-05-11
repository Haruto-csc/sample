N = int(input())
S = list(input())
data = [[0, 0]]
now = [0, 0]
ans = 'No'

for i in S:
    match i:
        case 'R':
            now[0] += 1
        case 'L':
            now[0] -= 1
        case 'U':
            now[1] += 1
        case 'D':
            now[1] -= 1
    for j in data:
        if now == j:
            ans = 'Yes'
            break
    data.append([now[0], now[1]])

print(ans)
