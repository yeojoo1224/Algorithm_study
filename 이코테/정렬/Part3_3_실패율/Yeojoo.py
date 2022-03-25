def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러있는 사람 수 계산
        user = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail_rate = 0
        else:
            fail_rate = user / length
        
        # 리스트에 (스테이지 번호, 살패율) 원소 삽입
        answer.append((i, fail_rate))
        length -= user
    
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer.sort(key = lambda x: x[1], reverse = True)
    
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer