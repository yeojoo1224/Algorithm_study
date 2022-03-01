import time
#data 입력
N,K=map(int,input().split())

cnt=0
start=time.time()
while(True):
        if N==1:
            break
        if N%K==0:
            N/=K
            cnt+=1
        else:
            N-=1
            cnt+=1
end=time.time()
print(cnt)
print("time:",start,end,end-start)