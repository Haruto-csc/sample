N = int(input())
x = 0
y = 0
for i in range(N):
    m = int(input())
    if (i % 4 == 0):
        y += m
    elif (i % 4 == 1):
        x += m
    elif (i % 4 == 2):
        y -= m
    else:
        x -= m

print(f'{x} {y}')
