n,c=map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))
data.sort()

s=data[0]
e=data[-1]
gap=e-s
result=0

while e>=s:
    mid=(s+e)//2
    cnt=1
    cv=data[0]
    for i in range(1,n):
        if data[i]>=cv+mid:
            cv=data[i]
            cnt+=1
    if cnt>=c:
        result=mid
        s=mid+1
    else:
        e=mid-1

print(result)

#답지봄. 
#생각하기 어려웠다... 복습필수일 듯