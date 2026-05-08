nl = list(map(int, input().split()))

data = [[] * nl[0]] * nl[1]
students = [0] * nl[1]

for i in range(nl[1]):
    data[i] = list(map(int, input().split()))

for i in range(nl[0]):
    m = data[0][i]
    stu = 0
    for j in range(nl[1]):
        if (m < data[j][i]):
            stu = j
            m = data[j][i]
    students[stu] += 1

print(f'{students.index(max(students))+1} {max(students)}')

