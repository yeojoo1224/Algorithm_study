from collections import deque

n,k=map(int,input().split())
graph=[]
virus=[[] for _ in range(k+1)] #바이러스 종류별 시작 위치
for i in range(n):
    tmp=list(map(int,input().split())) #시험관 한 행
    graph.append(tmp)
    for vi in range(n):
        if tmp[vi]!=0:
            virus[tmp[vi]].append((i,vi))
s,x,y=map(int,input().split())

#상하좌우
dx=[0,0,-1,1]
dy=[-1,1,0,0]

#초기 큐--> 초기 바이러스 위치 저장(작은 바이러스 순)
queue=deque()
for i in range(k+1):
    for j in virus[i]:
        queue.append((j,i,0))

time=0
#bfs구현
while(queue):
    data=queue.popleft()
    print(data)
    point=data[0]
    virus=data[1]
    t=data[2]
    time=t+1
    if time>s:
        break

    for i in range(4):
        nx=point[0]+dx[i]
        ny=point[1]+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
            graph[nx][ny]=virus
            queue.append(((nx,ny),virus,time))
        else:
            continue

print(graph[x-1][y-1])

#(답지안봄) 40분 소요
#dfs를 사용할 경우, 시간별로 가장 작은 바이러스부터 확산하기 어렵다.
#bfs를 사용하면, 가장 가까운 위치부터 탐색하므로 시간별로 가장 작은 바이러스부터 상하좌우 탐색이 가능하다.
