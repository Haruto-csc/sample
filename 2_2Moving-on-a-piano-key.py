S = list(input())
drm = ('d', 'r', 'm', 'f', 's', 'l', 'c')
now = 2
count = 0

for i in S:
    new = drm.index(i)
    count += abs(new - now) + 1
    now = new

print(count)
