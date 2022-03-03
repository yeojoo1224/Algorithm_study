# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0

    # 남은 음식의 개수
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        # 다 먹은 음식 제외
        length -= 1
        # 이전 음식 시간 재설정
        previous = now

    # 남은 음식중에서 몇번째 음식인지 확인하여 출력
    # 음식의 번호 기준으로 정렬
    result = sorted(q, key =  lambda x: x[1])
    return result[(k - sum_value) % length][1]


# 우선 순위 큐를 이용하지 않으면 시간 초과가 나는 문제라고 한댜
# 어쩐지 큐 안쓰고 나름 풀어보려고 했는데 잘 안되더라,,,
# 답지 보고 적긴 했는데 100퍼 이해는 안돼서 더 공부 해봐야겠다!!