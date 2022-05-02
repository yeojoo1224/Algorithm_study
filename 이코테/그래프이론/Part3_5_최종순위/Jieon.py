from collections import deque

test=int(input())
for _ in range(test):
    n=int(input())
    #진입차수 초기화
    indegree=[0]*(n+1)
    #간선정보 인접행렬 초기화
    graph=[[False]*(n+1) for i in range(n+1)]
    
    #작년순위정보 입력
    last_lank=list(map(int,input().split()))
    #간선정보 초기화
    for i in range(n):
        for j in range(i+1,n):
            graph[last_lank[i]][last_lank[j]]=True
            indegree[last_lank[j]]+=1

    #올해 변경된 순위정보 입력
    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split()) #a,b의 등수가 작년과 바뀜
        #간선방향 뒤집기
        if graph[a][b]: #작년에 a>b, 올해 b>a
            graph[a][b]=False 
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else: #작년에 b>a, 올해 a>b
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1

    #위상정렬 시작
    result=[]
    q=deque()

    #진입차수가 0인 노드를 넣어 초기화
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    
    certain=True #위상정렬 결과가 한개인지 여부
    cycle=False #사이클 방생 여부

    for i in range(n):
        if len(q)==0:
            cycle=True
            break
        if len(q)>=2:
            certain=False
            break

        now=q.popleft()
        result.append(now)
        #해당 원소와 ㅇㄴ결된 노드들의 진입차수에서 1빼기
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j]-=1
                #새롭게 진입차수가 0이 되는 노드 큐에 삽입
                if indegree[j]==0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()