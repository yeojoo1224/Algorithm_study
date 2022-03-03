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