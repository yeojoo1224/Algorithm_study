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
        if not pq: #더 섭취할 음식이 없는 경우
            return -1
        length = len(pq) #남은 음식의 개수
        time += (pq[0][0] - pre_food) * length #가장 시간이 작은 음식만큼 회전 돌기
        if time > k: #현재 시간이 k보다 클 경우, k이후 끝나는 지점을 탐색해야 함.
            time -= (pq[0][0] - pre_food) * length #시간을 k보다 작은 시간으로 되돌리기.
            while pq: #남은 음식 번호 넣기 (음식 번호 순으로 먹기 때문)
                answer_rs.append(heapq.heappop(pq)[1])
            answer_rs.sort()
            answer = answer_rs[(k - time) % length] #남은 시간을 통해 정답 구하기
            flag = False #return
        else:
            pre_food = heapq.heappop(pq)[0] #시간이 k보다 작으면, 회전 돌고, 다 먹은 음식 빼기
    return answer

    #복습
    def solution(food_times,k):
        pq=[]
        for i in range(len(food_times)):
            heapq.heappush(pq,[food_times[i],i+1])
        
        Flag=True
        time=0
        last=0
        last_foods=[]
        while Flag:
            if not pq: 
                return -1
            length=len(pq)
            time+=(pq[0][0]-last)*length
            if time>k:
                time-=(pq[0][0]-last)*length
                while pq:
                    last_foods.append(heapq.heappop(pq)[1])
                last_foods.sort()
                answer=last_foods[(k-time)%length]
                Flag=False
            else:
                last=heapq.heappop(pq)[0]
        return answer