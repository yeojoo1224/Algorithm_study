def solution(N,stages):
    fail=[0]*(N+2)
    p=0
    for c in stages: #딕셔너리에 스테이지에서 막힌 사람 수 저장
        fail[c]+=1
        p+=1

    for a in range(1,N+1): #실패율 계산
        if p==0: #분모가 0일경우, runtime error
            break
        tmp=fail[a] 
        fail[a]=float(fail[a])/p
        p-=tmp
    
    answer=sorted(range(1,len(fail)-1),key= lambda x: (-fail[x],x)) #실패율이 큰 순으로, stage가 작은순으로 인덱스 정렬
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
