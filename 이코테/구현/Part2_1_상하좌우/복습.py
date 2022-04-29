# 1. l, r, u ,d에 대해서 움직임에 대한 딕셔너리를 만든다. 
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

# 2. 공간의 크기, 이동 계획서 입력받기
n = int(input())
plan = list(map(str, input().split()))

# 3. 최종 도착 좌표를 (1, 1)으로 초기화
final = [1, 1]

# 4. 이동 계획서의 크기만큼 반복
for m in plan:

#   4-1. 이동계획을 하나씩 따지면서 이동할때마다 최종좌표 업데이트
    dx, dy = move[m]
    nx = final[0] + dx
    ny = final[1] + dy

#   4-2. 범위를 벗어나는 경우 무시 
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    final = [nx, ny]

# 5. 최종좌표 출력
print(final[0], final[1])


# Navigator: 이지언, Driver: 나여주