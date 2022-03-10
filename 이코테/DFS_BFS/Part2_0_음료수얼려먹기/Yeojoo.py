n, m = map(int, input().split())
ice = []
ice_cream = 0
for _ in range(n):
    ice.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
        # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        # 해당 노드 방문 처리
        ice[x][y] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            ice_cream += 1

print(ice_cream)

# 우선 0인 부분부터 따져야하므로 dfs로 풀어야겠다는 생각을 바로 했다!
# dfs()에서 주어진 범위를 벗어나는 경우를 생각하지 못했다
# dfs랑 bfs 개념이 워낙 많이 나오는만큼 문제를 많이 풀어서 익혀야겠다는 생각을 했다!