#driver: 지언 navigator: 여주
# 1. 동서남북 방향 정의 --> list
dx=[-1,0,1,0]
dy=[0,1,0,-1]
# 2. n,m 입력
n,m=map(int,input().split())
# 3. 처음 위치와 서 있는 방향 입력
a,b,d=map(int,input().split())
# 4. map1 리스트 0으로 초기화
map1=[[0]*m for _ in range(n)]
map1[a][b]=1
# 5. map2 리스트 입력
map2=[]
for i in range(n):
    map2.append(list(map(int,input().split())))
# 6. 왼쪽으로 회전하는 함수 생성
turn=[3,0,1,2]
def turn_left():
    global d
    d=turn[d]
    
# 7. cnt=0 초기화
cnt=1
# 8. while문 생성
flag=0
while(True):
#     9. 왼쪽회전 함수 실행
        turn_left()
#     10. 가보지 않은 칸이면 이동, cnt+=1
        nx=a+dx[d]
        ny=b+dx[d]
        if map1[nx][ny]==0 and map2[nx][ny]==0:
            map1[nx][ny]=1
            a=nx
            b=ny
            cnt+=1
            flag=0
            continue
#     10-1. 다 가본 칸이거나 바다일 경우, 왼쪽으로 회전
        elif map1[nx][ny]==1 or map2[nx][ny]==1:
            flag+=1
#     10-2. 네 방향 다 갈 수 없는 경우
        if flag==4 :
#         10-2-1. 뒤로 갈 수 있으면 뒤로 가기
            nx=a-dx[d]
            ny=b-dy[d]
            if map2[nx][ny]==0:
                a=nx
                b=ny
                flag=0
#         10-2-2. 갈 수 없으면 while문 break
            else:
                break
# 11. cnt 출력
print(cnt)
