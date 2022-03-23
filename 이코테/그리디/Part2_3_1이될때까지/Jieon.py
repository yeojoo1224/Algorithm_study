'''
import time
#data 입력
N,K=map(int,input().split())

cnt=0
while(True):
    #N이 K보다 작을 경우, -1만 남음
    if N<K:
        break
    
    #N이 K의 배수가 될 때 까지 -1하는 회수
    mul=(N//K)*K
    cnt+=N-mul
    N=mul

    #N//K 
    while(N%K==0):
        N//=K
        cnt+=1

cnt+=(N-1)
print(cnt)
'''
#복습
n,k=map(int,input().split())
cnt=0
while n>1:
    if n%k==0:
        n=n//k
        cnt+=1
    elif n>k:
        cnt+=(n%k)
        n-=n%k
    else:
        cnt+=n-1
        n=1

print(cnt)