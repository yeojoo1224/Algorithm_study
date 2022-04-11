from collections import deque
import copy

# 강의 수
N = int(input())
# 진입차수 0으로 초기화
indegree = [0] * (N + 1)
# 간선 정보 리스트
graph = [[] for i in range(N + 1)]
# 각 강의 시간 0으로 초기화
time = [0] * (N + 1)

# 모든 간선 정보
for i in range(1, N + 1):
    data = list(map(int, input().split()))  # 일단 리스트에 전부 담은 후
    time[i] = data[0] # 리스트의 첫 번째 수는 시간
    for x in data[1:-1]:  # 리스트의 두 번째 수부터 뒤에서 두번째까지는 선수과목 번호
        indegree[i] += 1  # 진입차수 증가시키고
        graph[x].append(i)  # 간선 정보에 담기


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 리스트의 값을 복사하는 함수
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들 확인
        for i in graph[now]:
            # 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면, 더 오랜 시간이 걸리는 경우의 시간 값을 저장
            result[i] = max(result[i], result[now] + time[i])
            # 연결된 노드들의 진입차수에서 1빼기
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    #위상 정렬 수행 결과 출력
    for i in range(1, N+1):
        print(result[i])

topology_sort()