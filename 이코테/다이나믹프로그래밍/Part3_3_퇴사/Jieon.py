n=int(input())
data=[]
for i in range(1,n+1):
    t,p=map(int,input().split())
    data.append((t,p))

dpt=[0]*(n+1)
max_v=0
for i in range(n-1,-1,-1):
    t=data[i][0]
    p=data[i][1]
    if i+t<=n:
        dpt[i]=max(p+dpt[i+t],max_v)
        max_v=dpt[i]
    else:
        dpt[i]=max_v
print(max_v)

#답지참조
#문제 어려워... 삼성 못가 ㅋㅋㅋㅋ

