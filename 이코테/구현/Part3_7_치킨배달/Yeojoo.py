from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n): # 도시 맵 정보를 입력받음
    a = list(map(int, input().split()))
    city.append(a)

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j]) # 일반 집
        elif city[i][j] == 2:
            chicken.append([i, j]) # 치킨 집

# 모든 치킨집 중에서 살아남는 m개의 치킨 집을 뽑는 조합 계산
live_chicken = list(combinations(chicken, m))

# 치킨 거리위 합을 계산하는 함수
def dist(live_chicken):
    distance = 0
    # 모든 집에 대하여
    for home_x, home_y in home:
        # 가장 가까운 치킨집을 찾기
        min_dist = 1000000000
        for chicken_x, chicken_y in live_chicken:
            min_dist = min(min_dist, abs(home_x - chicken_x) + abs(home_y - chicken_y))
        # 가장 가까운 치킨집까지의 거리를 더하기
        distance += min_dist
    # 치킨 거리의 합 반환
    return distance

# 치킨 거리의 합의 최소를 찾아 출력
distance = 1000000
for live_chick in live_chicken:
    distance = min(distance, dist(live_chick))

print(distance)

# 조합을 사용해야 할 것 같아서 인터넷을 참조해서 tool을 사용하였다
# 비교적 아이디어가 간단해서 스스로 풀수있었댜!!