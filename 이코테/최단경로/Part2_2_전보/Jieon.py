import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m,c=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
for i in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z)) #graph의 시작 노드에 (도착,거리) 간선 저장

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for node in graph[now]:
            cost=dist+node[1] #start에서 now노드를 거쳐 node[0]까지 가는 비용
            if cost<distance[node[0]]: 
                distance[node[0]]=cost
                heapq.heappush(q,(cost,node[0]))

dijkstra(c)

cnt=0
time=0
for i in range(n+1):
    if distance[i]<INF:
        cnt+=1
        time=max(time,distance[i])

cnt-=1 #자기자신 제외

print(cnt,time)
