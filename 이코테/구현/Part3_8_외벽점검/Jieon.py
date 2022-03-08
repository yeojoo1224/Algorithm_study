from itertools import permutations
def solution(n, weak, dist):
    w_len=len(weak)
    for i in range(w_len):
        weak.append(weak[i]+n) #2배로 늘리기
    
    answer=len(dist)+1 #총 친구 수+1
    
    for start in range(w_len): #시작점을 0부터 weak의 마지막 위치까지로 변경해가며 비교
        for friends in list(permutations(dist,len(dist))): #친구 순서를 순열로 표현
            cnt=1
            f_end=weak[start]+friends[cnt-1] #첫번째 친구의 마지막 확인 위치
            for index in range(start,start+w_len): #시작점부터 마지막 취약점까지 차례대로 확인
                if f_end < weak[index]: #검사 인원 추가
                    cnt+=1
                    if cnt>len(dist): #친구가 부족할 경우
                        break
                    f_end=weak[index]+friends[cnt-1]  #추가된 친구의 마지막 확인 위치
            answer=min(answer,cnt)
    
    if answer>len(dist):
        return -1
    else:
        return answer

#완전 답지봄. 
#1. 원형 데이터 처리 형태 --> 배열 2배로 증가
#2. 친구를 순열로 배열하여 비교했어야 하는 문제.
# 어려웠다.