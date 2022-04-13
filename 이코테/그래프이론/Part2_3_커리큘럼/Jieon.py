from collections import deque
import copy

n=int(input())
#진입차수
indegree=[0]*(n+1)
#연결리스트
graph=[[] for _ in range(n+1)]
#각 강의 시간
time=[0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

#위상정렬함수
def topology_sort():
    result=copy.deepcopy(time)
    q=deque()

    #처음시작시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    
    #큐가 빌 때 까지
    while(q):
        now=q.popleft()
        #해당 원소와 연결된 노드들의 진입차수 빼기, 현재 노드 삭제
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            #새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i]==0:
                q.append(i)
    
    for i in range(1,n+1):
        print(result[i])

topology_sort()

#답지봄