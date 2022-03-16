from collections import deque
#input data
n,l,r=map(int,input().split())
people=[]
for _ in range(n):
    people.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(sx,sy,index):
    queue=deque()
    queue.append((sx,sy))
    
    united=[]
    united.append((sx,sy))
    sum_p=people[sx][sy]
    cnt=1
    #union변수
    union[sx][sy]=index
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(people[x][y]-people[nx][ny])<=r:
                    queue.append((nx,ny))
                    union[nx][ny]=index
                    united.append((nx,ny))
                    sum_p+=people[nx][ny]
                    cnt+=1
    for i, j in united:
        people[i][j]=sum_p//cnt
    return cnt

time=0
while True:
    union=[[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                bfs(i,j,index)
                index+=1
    if index==n*n:
        break
    time+=1

print(time)

# 답지봄.
# 너무 어려웠다.
# 조금 입체적으로 생각했어야 했다. 
# 처음에 연합이 한개만 나오는줄 알고 bfs와 union 리스트까지 생각하고, union 배열은 생각 못했다. 
'''하지만 생각해보니 연합이 여러개 나올 수 있고, union을 리스트가 아닌 2차원 배열로 만들어야 했고, 
   스타트 포인트를 모든 배열의 원소로 설정하여 union이 없는 경우 bfs를 통해 배열을 다 점검한 뒤, time을 증가시켰어야 했다.'''
# 그 부분을 구현하는 것이 잘생각이 나지 않았고, 답지를 보았다. 다시 풀라고 하면 쉽게 풀 수 있을 것 같다.