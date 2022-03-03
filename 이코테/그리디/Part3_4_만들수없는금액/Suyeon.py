n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True) #그리디 적용: 가장 큰 배열 값부터 빼기 위해 내림차순 정렬

num=0 #계산할 변수 
origin=0 #계산 하기 전 원래 값을 저장할 변수

# 원래 값을 저장하는 변수는 값 계속 증가, 값이 변화하는 num에 원본 값을 받아서 계산 진행
# 그리디를 적용해서 가장 큰 수 부터 빼주고, 다 뺏을 때 값이 0이 아닌 첫번째 수를 출력하고 반복문 빠져나감
while True:
    origin+=1
    num = origin
    for i in s:
        if i<=num:
            num-=i
            if num==0:
                break
        else:
            continue
    
    if num!=0:
        print(origin)
        break

