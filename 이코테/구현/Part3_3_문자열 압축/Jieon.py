s=str(input())
answer = 0
length=len(s) #문자열 길이
window_cnt=[] #slice 크기별 압축문자 길이 저장

for i in range(1,length+1):         
    window=s[0:i] #슬라이싱 윈도우 초기화
    pre=0 #이전 슬라이스 마지막 부분
    comp_term=[] #압축한 문장 저장
    cnt=0 #슬라이스 반복 회수 세기
    for e in range(pre+i,length+1,i):
        if window==s[pre:e]: #이 전 슬라이스와 동일한 경우
            cnt+=1
        else: #이 전 슬라이스와 다른 경우
            if cnt!=1: #이 전 압축 
                comp_term.append(str(cnt))
            #이 전 슬라이스 문장 저장
            comp_term.append(s[pre-i:pre])
            window=s[pre:e] #비교 윈도우 갱신
            cnt=1 #비교 윈도우 횟수 갱신                   
        pre=e #비교 슬라이스 위치 갱신

    #마지막 슬라이스 저장   
    if cnt!=1:
        comp_term.append(str(cnt)) #압축가능 할 경우
    comp_term.append(window) #압축과 관계없이 슬라이스 문장 저장

    #압축한 문장 길이 저장 (i만큼 슬라이스할 때 마다)
    cnt_i=len("".join(comp_term))+(length%i) #슬라이스 길이에 맞지 않아 남겨진 문장 길이도 추가
    window_cnt.append(cnt_i)  #압축된 문장 길이 저장            

answer=min(window_cnt) #가장 짧은 압축문장 길이 출력
print(answer)