from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))   

# 이동할 4 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n - 1][m - 1]

print(bfs(0, 0))