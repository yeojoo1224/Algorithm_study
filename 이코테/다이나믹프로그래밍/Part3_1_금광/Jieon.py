t=int(input())
dx=[-1,0,1]
for _ in range(t):
    #input data
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    #spit data -> mine array(nXm)
    mine=[]
    for i in range(0,len(data),m):
        mine.append(data[i:i+m])
    
    #bottom-up
    array=[[0]*m for _ in range(n)] #dp table
    for j in range(n): #set column[0] 
        array[j][0]=mine[j][0]

    answer=0
    for y in range(1,m): #column 변경
        for x in range(n): #row 변경
            max_v=0
            for i in range(3): #x,y로 옮기기 전 모든 위치 확인
                nx=x+dx[i]
                ny=y-1
                if 0<=nx<n and 0<=ny<m:
                    max_v=max(max_v,array[nx][ny]+mine[x][y])
            array[x][y]=max_v #가장 큰 금 크기 저장
            answer=max(answer,max_v) #전체 경우 비교
    print(answer)

#답지 안봄
#처음에 마지막 n,m위치에서의 가장 큰 금의 개수를 구하는줄 알았다... 그래서 top-down방식을 사용했는데, 문제를 잘 보니 초기&최종 위치는 자율적이었다.
#그래서 모든 위치에서 가장 큰 금의 개수를 구해야 하기 때문에, bottom-up방식으로 모든 경우를 확인해야 했다.
#재미있는 문제였고, 다음부터 문제를 잘 읽어야 겠다.ㅋㅋ


