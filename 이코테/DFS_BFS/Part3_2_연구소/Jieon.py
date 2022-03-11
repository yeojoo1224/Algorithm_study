#구현(전체 경우의 수 확인) &dfs
from itertools import combinations
import copy

n,m=map(int,input().split())
graph=[]
zero=[]
two=[]
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)
    for j in range(m):
        if graph[i][j]==0:
            zero.append((i,j))
        if graph[i][j]==2:
            two.append((i,j))

dx=[0,0,-1,1]
dy=[-1,1,0,0]          
def dfs(node,graph):
    r=node[0]
    c=node[1]
    if graph[r][c]==0:
        graph[r][c]=2
        for i in range(4):
            if r+dx[i]>-1 and r+dx[i]<n and c+dy[i]>-1 and c+dy[i]<m: #실수한 부분
                dfs((r+dx[i],c+dy[i]),graph)
            else:
                continue
        return True
    else:
        return False

answer=0
com_zero=list(combinations(zero,3))
for new_wall in com_zero:
    tmp_graph=copy.deepcopy(graph)
    for i in range(3):
        r=new_wall[i][0]
        c=new_wall[i][1]
        tmp_graph[r][c]=1
    for virus in two:
        tmp_graph[virus[0]][virus[1]]=0
        dfs(virus,tmp_graph)
    tmp=0
    for i in range(n):
        tmp+=tmp_graph[i].count(0)
    if tmp>answer:
        answer=tmp

print(answer)

#답지안봄 소요: 80분
#dfs를 사용하고, 재귀함수를 활용하여 멀리 떨어진 곳 부터 확인한다. 
#오래 걸린 이유는 실수를 해서 오류가 생겼었다. and가 아닌 or을 사용했기 때문에 오류가 났었다.ㅋㅋ
#기존 dfs와 다른 점은 구현 문제와 혼합이 되었던 것이다. 3개의 벽을 선택할 경우의 수를 모두 고려하여 바이러스를 전파시켜 가장 큰 안정영역을 비교했어야 했다.
#코드 짤 때 아무리 내 머릿속에 있더라도 항상 실수를 유의하며 구현해야겠다.