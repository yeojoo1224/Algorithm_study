from collections import deque

n, l, r = map(int, input().split())
country = []
for i in range(n):
    country.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    # 국경선을 공유하는 국가들의 좌표 삽입
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구수 차이가 조건을 만족하면, 국경선을 연다.
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp


cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                # 조건을 만족하여 국경선이 열렸다면, 인구 이동을 시작한다
                if len(temp) > 1:
                    isTrue = True
                    # 연합을 이루고 있는 각 칸의 인구수를 구한다
                    num = sum([country[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        country[x][y] = num
    # 연합을 해체하고, 모든 국경선을 닫는다.
    if not isTrue:
        break
    cnt += 1
print(cnt)

# 문제를 확인했을 때 bfs를 사용해야한다고 생각을 했다.
