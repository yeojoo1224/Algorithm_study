import heapq
import sys
input=sys.stdin.readline

INF=int(1e9)
n,m=map(int,input().split())
graph=[[] for _  in range(n+1)]
result=[INF]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q=[(0,1)] #dist,b
result[1]=0
while(q):
    dist,b=heapq.heappop(q)
    if result[b]<dist:
        continue
    for node in graph[b]:
        cost=dist+node[1]
        if result[node[0]]<cost:
            continue
        result[node[0]]=cost
        heapq.heappush(q,(cost,node[0]))

max_d=0
cnt=0
for i in range(2,n+1):
    if result[i]==max_d:
        cnt+=1
    elif max_d<result[i] and result[i]<INF:
        answer_i=i
        max_d=result[i]
        cnt=1

print(answer_i,max_d,cnt, end=' ')