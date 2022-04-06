INF = int(1e9)
n, m = map(int, input().split())

score = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    score[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    score[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            score[j][k] = min(score[j][k], score[j][i] + score[i][k])

result = 0
count = 0

# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (score[i][j] != 0 and score[i][j] != INF) or (score[j][i] != 0 and score[j][i] != INF):
            count += 1  
    if count == n - 1:
        result += 1
    count = 0

print(result)