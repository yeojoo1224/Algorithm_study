from collections import deque
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)] #간선정보 저장

for _ in range(m): #간선 입력
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(x,graph):
    queue=deque() #queue생성
    visit=[0]*(n+1) 
    cnt=[0]*(n+1) #노드별 x와의 거리 저장
    answer=[]
    #초기 위치 저장
    queue.append(x)
    visit[x]=1
    #bfs탐색
    while queue:
        node=queue.popleft()
        for i in graph[node]: #pop한 node와 연결된 node탐색
            if visit[i]==0: #연결된 노드가 방문한 적 없다면,
                queue.append(i)
                visit[i]=1
                cnt[i]=cnt[node]+1 #거리 저장
                if cnt[i]==k: #해당 거리가 k라면
                    answer.append(i)
    return answer

result=sorted(bfs(x,graph))
if result:
    for i in result:
        print(i)
else:
    print(-1)

#답지안봄, 23분 소요
#이 문제는 간단하게 생각 할 수 있었다. 
#가장 가까운 노드부터 탐색하면서 한 계층이 끝날 때 마다 깊이가 늘어나므로, 거리가 +1만큼 늘어난다.
#따라서 bfs를 사용하면서 한 계층이 시작할 때 마다 거리(cnt)를 늘려주고, 새로운 노드를 만나면 queue에 저장한다.
#그 거리가 내가 찾는 거리(k)이고, 그 거리에서 새로운 노드가 탐색된다면, 그 노드가 내가 찾는 도시가 된다.