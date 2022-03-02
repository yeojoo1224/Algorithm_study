n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
# 현재 좌표를 방문처리하기 위해 0->1로 바꾸어주기
d[x][y] = 1

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 입력
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 있는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우(갈 수 없는 경우)
        else:
            break
        turn_time = 0

print(count)

# 1번과 3번 문제와 유사하다고 생각했으나 고려할 점이 많아서 까다로웠다.
# 어떤 요구사항부터 어떻게 처리해야 할 지 바로 파악하기가 힘들었다.
# 답지를 참조하여 작성하였는데 좀 더 자세히 다시 보면서 외워야겠다!
# 중간에 '=' 적어야 하는 부분에서 '=='적어서 입력하는 부분에서 5줄만 입력받아야 하는데 끝없이 입력 받았다...