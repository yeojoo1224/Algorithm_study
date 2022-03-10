import sys
#정보 받기
n,m=map(int,sys.stdin.readline().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,input())))

#상하좌우 움직임
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def move(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재노드 방문가능
    if maze[x][y]==0:
        maze[x][y]=1
        #상하좌우 재귀 호출
        for i in range(4):
            move(x+dx[i],y+dy[i])
        return True
    else:
        return False

#음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        if move(i,j):
            result+=1

print(result)

#답지 참조
#stack이 필요한 DFS탐색은 아니었지만, 재귀함수를 사용한다는 점에서 DFS라고 표현한 듯.
#그래프와 재귀함수가 너무 오랜만이라 감이 잘 잡히지 않았다.
#다른 문제를 풀어보며 익혀야 할 듯...