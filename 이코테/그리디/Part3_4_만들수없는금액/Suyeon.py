n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True) #그리디 적용: 가장 큰 배열 값부터 빼기 위해 내림차순 정렬

num=0 #계산할 변수 
origin=0 #계산 하기 전 원래 값을 저장할 변수

# 원래 값을 저장하는 변수 origin은 1부터 값 계속 증가(1,2,3,4,...), 값이 변화하는 num에 origin 값을 받아서 계산 진행
# origin=1부터 어떤 수(첫번째 수)까지 그리디를 적용해서 가장 큰 수 부터 빼주고, 다 뺏을 때 값이 0이 아닌 첫번째 수를 출력하고 반복문 빠져나감
while True:
    origin+=1 #만들수 없는 '최소' 금액이므로 1부터 탐색(s에 들어있는 수들로 1을 만들 수 있는지 없는지)
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

