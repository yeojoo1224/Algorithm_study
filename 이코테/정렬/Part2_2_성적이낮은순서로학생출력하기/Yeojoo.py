n = int(input())
array = []

for _ in range(n):
    student_grade = input().split()
    array.append((student_grade[0], int(student_grade[1])))

array.sort(key=lambda x:x[1])

for x in array:
    print(x[0], end = ' ')