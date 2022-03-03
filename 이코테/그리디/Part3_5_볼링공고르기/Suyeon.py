#두 사람이 서로 다른 볼링공 선택하는 경우의 수 구하기
#공의 번호는 순서대로 부여
#공의 무게는 1~M까지 자연수 형태로 존재
n,m = map(int, input().split())
s = list(map(int, input().split()))
count = {}
result = (n*(n-1))//2

if m==1: 
    result =0
else:
    #주어진 리스트에서 각 요소별 개수 세고 저장하는 count 딕셔너리 생성
    for i in s:
        try: count[i]+=1
        except: count[i]=1

    #count 딕셔너리에서 값만 추출해서 다시 리스트로 변환
    new_s = list(count.values())

    #리스트에서 중복되는 요소는 원래 수에서 중복되는 수의 nC2해서 뺀다
    for i in new_s:
        if i==n:
            result = 0
        elif i>1:
            result -= (i*(i-1))//2


print(result)
