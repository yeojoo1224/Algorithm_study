import heapq
INF=1e9

dx=[-1,1,0,0]
dy=[0,0,-1,1]

t=int(input())
for _ in range(t):
    n=int(input())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))

    dist=[[INF]*n for _ in range(n)]

    q=[(graph[0][0],0,0)]
    dist[0][0]=graph[0][0]

    while q:
        d,x,y=heapq.heappop(q)
        if dist[x][y]<d:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost=d+graph[nx][ny]
                if cost<dist[nx][ny]:
                    dist[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))
                else:
                    continue
    print(dist[n-1][n-1])

#답지봄

