#답지 일부 적용, 프로그래머스 대부분 정답. (어디가 문제일까?)
import heapq
def solution(food_times, k):
    if sum(food_times)<k:
        return -1
    
    length=len(food_times) #전체 시간 개수
    left=[] #힙에 남아 있는 시간들
    for i in range(length):
        heapq.heappush(left,(food_times[i],i+1))
    
    prev=0 #가장 작은 시간부터
    while(((left[0][0]-prev)*length)<k):
        now=heapq.heappop(left)[0] #가장 작은 시간 빼기
        k-=((now-prev)*length) #총 시간 감소
        length-=1
        prev=now #prev 업데이트
    
    result=sorted(left,key=lambda x:x[1]) #음식 번호 기준으로 재정렬
    answer=result[k%length][1]
    
    return answer


#프로그래머스 정답 --------------
def solution(food_times, k):
    answer = 0
    time = 0
    pq = []
    answer_rs = []
    # 1. 우선순위 큐에 (food_times, 음식 번호) 순으로 담는다.
    for i in range(len(food_times)):
        heapq.heappush(pq, [food_times[i], i + 1])

    pre_food = 0
    flag = True
    while flag:
        if not pq:
            return -1
        length = len(pq)
        time += (pq[0][0] - pre_food) * length
        if time > k:
            time -= (pq[0][0] - pre_food) * length
            while pq:
                answer_rs.append(heapq.heappop(pq)[1])
            answer_rs.sort()
            answer = answer_rs[(k - time) % length]
            flag = False
        else:
            pre_food = heapq.heappop(pq)[0]
    return answer