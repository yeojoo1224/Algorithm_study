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

print(result)