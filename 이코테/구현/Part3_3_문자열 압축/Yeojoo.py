def solution(s):
    answer = len(s)
    # 1개의 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step)만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축시키지 못하는 경우라면)
            else:   
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리 
        compressed += str(count) +prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))  
    return answer

# 한 시간 넘게 헤맸지만 결국 답지를 본 문제 흑흑,,,
# 카카오 입사 문제는 언제쯤 내 힘으로 풀수있을까,,,