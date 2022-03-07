n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
rotation = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    apple_row, apple_col = map(int, input().split())
    board[apple_row][apple_col] = 1

# 방향 회전 정보 입력
l = int(input())
for i in range(l):
    x, c = input().split()
    rotation.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 곳은 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 초 시간
    index = 0 # 다음에 회전할 정보
    snake = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                snake.append((nx, ny))
                px, py = snake.pop(0)
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면    
        else:
            time += 1
            break

        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < 1 and time == rotation[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, rotation[index][1])
            index += 1
    return time

print(simulate())

# 맵 정보와 회전 정보는 잘 입력 받았다
# 생각은 잘 하는데 코드로 구현하기가 참 어렵다ㅠㅠ
# 앞선 문제랑 이거랑 답지 안보고 다시 풀어봐야겠다,,,