a = list(map(int, input().split()))
N = a[0]
Q = a[1]
member = [0] * N
ejection = []

for i in range(Q):
    b = list(map(int, input().split()))
    match b[0]:
        case 1:
            member[b[1] - 1] += 1
        case 2:
            member[b[1] - 1] += 2
        case 3:
            if (member[b[1] - 1] >= 2):
                ejection.append('Yes')
            else:
                ejection.append('No')

for j in range(len(ejection)):
    print(ejection[j])
