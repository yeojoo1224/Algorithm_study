#딥지안봄
import sys
from collections import deque

N=int(sys.stdin.readline()) #보드의 크기
board=[[0]*(N+2) for _ in range(N+2)]

#보드 가장자리 벽처리(2)
board[0]=[2]*(N+2) 
board[N+1]=[2]*(N+2)
for i in range(N+2):
    board[i][0]=2
    board[i][N+1]=2

K=int(sys.stdin.readline()) #사과의 개수
for _ in range(K):
    x,y=map(int,sys.stdin.readline().split())
    board[x][y]=1 #사과의 위치

L=int(sys.stdin.readline()) #방향 변환 정보
trans_inform=deque()
for _ in range(L): #방향 변환 정보 저장
    t,d=map(str,sys.stdin.readline().split())
    t=int(t)
    trans_inform.append([t,d])

#next (오른쪽 방향 변환 순서)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

direction=0
snake=deque()
snake.append([1,1])
time=0
while(True):
    next_x=snake[-1][0]+dx[direction]
    next_y=snake[-1][1]+dy[direction]
    next_head=[next_x,next_y]

    time+=1

    if board[next_x][next_y]==2: #만약 벽을 만난다면
        break
    if next_head in snake: #만약 몸통과 부딪친다면
        break

    snake.append(next_head) #head 이동

    if board[next_x][next_y]==0: #만약 사과가 없다면, 꼬리 자르기
        snake.popleft()
    else: #사과가 있다면, 사과 먹어버리기
        board[next_x][next_y]=0
    
    #방향 변환시기
    if trans_inform and time==trans_inform[0][0]:
        trans=trans_inform.popleft()
        if trans[1]=='L':
            direction-=1
            direction=direction%-4
        elif trans[1]=='D': 
            direction+=1
            direction=direction%4

print(time)