n=int(input())
data=list(map(int,input().split()))

dpt=[1]*n

answer=0
for i in range(1,n):
    for j in range(0,i):
        if data[j]>data[i]:
            dpt[i]=max(dpt[j]+1,dpt[i])
print(n-max(dpt))

#답지 참조...