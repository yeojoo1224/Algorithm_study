#답지 안봄
#의문점: A,B=(1번공,2번공) , A,B=(2번공, 1번공) 다른 경우 아닌가?ㅋㅋㅋ 
import sys

N,M=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

count=list(0 for _ in range(M+1)) #무게별 볼링공 개수
for i in data:
    count[i]+=1

tmp=count[M] #가장 무거운 볼링공부터 고려
result=0
for i in range(M-1,0,-1): #경우의 수 구하기
    result+=count[i]*tmp 
    tmp+=count[i] 

# 답지(best)
import sys

N,M=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

count=list(0 for _ in range(M+1)) #무게별 볼링공 개수
for i in data:
    count[i]+=1

result=0
for i in range(1,M+1):
    N-=count[i]
    result+=count[i]*N
print(result)


#복습
'''
n,m=map(int,input().split())
data=list(map(int,input().split()))

from itertools import combinations
comb=list(combinations(range(0,n),2))
result=0
for cand in comb:
    b1=cand[0]
    b2=cand[1]
    if data[b1]!=data[b2]:
        result+=1

print(result)'''