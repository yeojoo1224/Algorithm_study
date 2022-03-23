import sys
#N,M,K 받기
N,M,K=map(int,sys.stdin.readline().split())
#N개의 수 받기
num=list(map(int,sys.stdin.readline().split()))

num.sort() #num_list 정렬
num1=num[-1] #가장 큰 수
num2=num[-2] #두번째로 큰 수

result=(num1*K+num2)*(M//(K+1))+num1*(M%(K+1)) #num1&num2의 반복성 활용
 
print(result)

#복습
n,m,k=map(int,input().split())
numbers=sorted(list(map(int,input().split())),reverse=True)
num1=numbers[0]
num2=numbers[1]
index=1
answer=0
while index<m+1:
    if index%(k+1)>0:
        answer+=num1
    else:
        answer+=num2
    index+=1
print(answer)
