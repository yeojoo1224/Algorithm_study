from collections import deque
def move(pos,board):
    next_pos=[]
    pos=list(pos)
    pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]

    #상하좌우 움직임
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        n_pos1_x, n_pos1_y=pos1_x+dx[i],pos1_y+dy[i]
        n_pos2_x,n_pos2_y=pos2_x+dx[i],pos2_y+dy[i]
        if board[n_pos1_x][n_pos1_y]==0 and board[n_pos2_x][n_pos2_y]==0:
            next_pos.append({(n_pos1_x,n_pos1_y),(n_pos2_x,n_pos2_y)})

    #회전
    if pos1_x==pos2_x: #로봇이 가로로 누워있는 경우
        for i in [1,-1]:
            if board[pos1_x+i][pos1_y]==0 and board[pos1_x+i][pos2_y]==0: #위,아래가 모두 비어있는 경우
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)}) #pos1을 축으로 90도 회전
                next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)}) #pos2 ""
    elif pos1_y==pos2_y: #로봇이 세로로 서 있는 경우
        for i in [1,-1]:
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0: #왼쪽, 오른쪽이 모두 비어 있는 경우
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)}) #pos1을 축으로 90도 회전
                next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)}) #pos2를  ""

    return next_pos

def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]
    
    #bfs
    q=deque()
    visited=[]
    pos={(1,1),(1,2)} #시작위치
    q.append((pos,0))
    visited.append(pos)

    while q:
        pos, cost=q.popleft()
        if (n,n) in pos:
            return cost
        
        for next_pos in move(pos,new_board):
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)
        
    return 0

#답지
#bfs로 풀면 되는 문제였는데, 회전 부분도 어떻게 구현해야 할지 감이 안잡혔다. 가로,세로,축의 위치에 따라 경우의 수가 너무 다 달라서 그랬던 것 같다.
#하지만 차분히 생각해보면 풀 수 있는 문제였던 것 같다. 다음부턴 다시 차분히 생각하는 시간을 가져야 할 것 같다.