import sys
#N,M,K 받기
N,M,K=map(int,sys.stdin.readline().split())
#N개의 수 받기
num=list(map(int,sys.stdin.readline().split()))

num.sort() #num_list 정렬
num1=num[-1] #가장 큰 수
num2=num[-2] #두번째로 큰 수

result=0

while True:
    for i in range(K):
        if M==0:
            break
        result+=num1
        M-=1
    if M==0:
        break
    result+=num2
    M-=1

print(result)