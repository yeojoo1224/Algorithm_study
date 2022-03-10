import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    #초기(1,1)일 때, queue 생성 및 저장
    queue=deque()
    queue.append((x,y))

    #queue가 남아있을 때 까지 
    while queue:
        x,y=queue.popleft() 
        #네 방향 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if maze[nx][ny]==0: #괴물이 있을 경우
                continue
            if maze[nx][ny]==1: #처음 방문일 경우
                maze[nx][ny]+=maze[x][y]
                queue.append((nx,ny))
    
    return maze[n-1][m-1]

print(bfs(0,0))

#답지참조
#그래프와 탐색 문제는 아직 어렵다.
#bfs의 경우, 가장 가까운 노드부터 확인한다. 
#보통 bfs는 queue를 사용하고, 노드와 인접한 노드들을 queue에 저장하고, 가장 가까운(숫자가 가장 작은)노드[front]부터 pop해서 확인한다.
#하지만 미로문제의 경우, 인접노드를 알 수 있는 그래프가 아니기 때문에, 인접노드를 직접 상하좌우로 탐색하여 찾아서 queue에 저장해야 하는 문제였다.
#탐색이 다 끝났다는 것은 queue에 아무 수도 남아있지 않는 경우이다.