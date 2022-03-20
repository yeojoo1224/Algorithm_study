n = int(input())
array = [] # 학생이름과 점수를 입력받는 리스트

for _ in range(n):
    score = input().split()
    # 이름과 국영수 점수를 리스트에 담는다
    array.append((score[0], int(score[1]), int(score[2]), int(score[3])))

# lamda를 이용하여 주어진 조건에 맞게 정렬한다.
array.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

# 학생의 이름을 출력한다.
for x in array:
    print(x[0])