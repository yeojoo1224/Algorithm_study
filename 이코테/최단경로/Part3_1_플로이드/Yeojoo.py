INF = int(1e9)

n = int(input())
m = int(input())

bus = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    bus[i][i] = 0

# 각 간선에 대한 정보를 입력 받음
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    bus[a][b] = min(bus[a][b], cost)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 0을 출력
        if bus[a][b] == INF:
            print(0, end = ' ')
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(bus[a][b], end = ' ')
    print()