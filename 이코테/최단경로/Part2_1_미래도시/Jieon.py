INF=1e9
n,m=map(int,input().split())

data=[[INF]*(n+1) for _ in range((n+1))]
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            data[a][b]=0

for i in range(m):
    a,b=map(int,input().split())
    data[a][b]=1
    data[b][a]=1

x,k=map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            data[a][b]=min(data[a][b],data[a][k]+data[k][b])

d_1k=data[1][k]
d_kx=data[k][x]
if d_1k>=INF or d_kx>=INF:
    print(-1)
else:
    print(d_1k+d_kx)