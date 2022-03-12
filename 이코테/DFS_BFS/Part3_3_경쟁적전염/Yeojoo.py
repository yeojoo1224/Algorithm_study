from collections import deque

N, K = map(int, input().split())
area = [] # 전체 맵 정보를 담는 리스트
virus = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        # 해당 위치에 바이러스가 있는 경우
        if area[i][j] != 0:
            # 바이러스 종류, 위치 X, 위치 Y 삽입
            virus.append((area[i][j], i, j))

S, X, Y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s, x, y):
    q = deque(virus)
    time = 0
    while q:
        # 입력한 초가 지나면 종료
        if time == S:
            break
        else:
            for _ in range(len(q)):
                num, x, y = q.popleft()
                # 현재 노드에서 주변 4가지 위치를 각각 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 해당 위치로 이동할 수 있는 경우
                    if 0 <= nx < N and 0 <= ny < N:
                        # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
                        if area[nx][ny] == 0:
                            area[nx][ny] = area[x][y]
                            q.append((area[nx][ny], nx, ny))
            # 바이러스를 퍼트린 후에 시간을 증가시킨다
            time += 1    
    return area[X - 1][Y - 1]

virus.sort()
print(bfs(S, X, Y))

# 답지 안보고 풀었다!