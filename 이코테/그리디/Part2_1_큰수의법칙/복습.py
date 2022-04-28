#1. n,m,k입력
n,m,k=map(int,input().split())

#2. n개의 수를 입력받는다. -> 리스트로 입력받기
data=list(map(int,input().split()))
data.sort()
#3. 가장 큰 수와 두번째로 큰 수를 찾아낸다
num1=data[-1]
num2=data[-2]
#4. 정답값을 0으로 초기화
answer=0
'''
#5. 반복문 생성, 반복 중에 m==0이면 반복문 탈출
    #5-1. 가장 큰 수를 정답값에 k번 더하고, 더하는 반복 수 만큼 m을 1씩 차감
    #5-2. 두번째로 큰 수를 정답값에 한 번 더해준다. 더할 때 마다 m을 1씩 차감
while m>0:
    for _ in range(k):
        if m==0:
            break
        answer+=num1
        m-=1
    if m==0:
        break
    answer+=num2
    m-=1

#6. 정답값 출력
print(answer)'''

#5 수학적으로 계산하여 문제해결 [num1*k+num2] 반복횟수로 계산
cnt=m//(k+1)
cnt_r=m%(k+1)
answer=(num1*k+num2)*cnt+num1*cnt_r
print(answer)

#navigator: 여주, driver:지언