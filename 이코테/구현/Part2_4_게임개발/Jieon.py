'''import sys
n,m=map(int,sys.stdin.readline().split())
a,b,d=map(int,sys.stdin.readline().split())
data=[]
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

nd=[3,0,1,2]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
had=[[0]*m for _ in range(n)] #가 본 경우>1

now=(b,a) #현재위치
had[b][a]=1

result=1
turn_time=0
while(True):
    nx=now[0]+dx[d]
    ny=now[1]+dy[d]
    d=nd[d] #방향변경
    if (nx>=0 and nx<m) and (ny>=0 and ny<n): 
        if data[ny][nx]==0 and had[ny][nx]==0: #바다도 아니고, 가본적도 없는 경우
            had[ny][nx]=1
            now=(nx,ny)
            result+=1
            turn_time=0
        else: #바다이거나, 가본적 있는 경우
            turn_time+=1
        if turn_time==4: #사방이 바다이거나 가본 적 있는경우
            turn_time=0
            nx=now[0]+dx[nd[d]]
            ny=now[1]+dy[nd[d]]
            if data[ny][nx]==0: #뒤가 바다가 아닐 경우
                now=(nx,ny)
            else: #뒤가 바다일 경우
                break
    else: 
        print('error')
        break

print(result)'''

#복습
#데이터 받기
n,m=map(int,input().split())
x,y,d=map(int,input().split())
point=[x,y,d]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

def rotate(point):
    left_d=[3,0,1,2]
    next_d=left_d[point[2]]
    point[2]=next_d
    return point

next=[(-1,0),(0,1),(1,0),(0,-1)]
back=[(1,0),(0,-1),(-1,0),(0,1)]

flag=True
cnt=1
answer=1
graph[point[0]][point[1]]=2
point=rotate(point)

while flag:
    dx=next[point[2]][0]
    dy=next[point[2]][1]
    next_p=(point[0]+dx,point[1]+dy)
    if 0<=next_p[0]<n and 0<=next_p[1]<m:
        if graph[next_p[0]][next_p[1]]==0:
            cnt=0
            point=[next_p[0],next_p[1],point[2]]
            graph[next_p[0]][next_p[1]]=2
            answer+=1
        else:
            point=rotate(point)
            cnt+=1
        if cnt==4:
            bx=point[0]+next[point[2]][0]
            by=point[1]+next[point[2]][1]
            if graph[bx][by]==1:
                flag=False
            else:
                cnt=0
                point=[bx,by,point[2]]

print(answer)

        

            