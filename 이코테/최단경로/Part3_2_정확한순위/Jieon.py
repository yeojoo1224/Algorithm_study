n,m=map(int,input().split())

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
#graph data 받기
for i in range(m):
    a,b=map(int,input().split()) #a<b
    graph[a][b]=-1
    graph[b][a]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]==graph[k][b] and -1<=graph[a][k]<=1: #((a<k and k<b) or (a>k and k>b)알 경우, a<b or a>b)
                graph[a][b]=graph[a][k]
                graph[b][a]=-graph[a][k]

answer=0   
for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        if -1<=graph[i][j]<=1:
            cnt+=1
    if cnt==n:
        answer+=1
print(answer)

#답지 안봄. 
#최단경로로는 풀지 않았지만, 플루이드 워셜처럼 2차원 배열과 DP점화식을 사용해봤다. 
#난 좀 더 직관적인 코드를 좋아하는 것 같다.