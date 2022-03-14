from itertools import combinations
n=int(input())
data=[]
X=[]
T=[]
for i in range(n):
    tmp_d=list(map(str,input().split()))
    data.append(tmp_d)
    for j in range(n):
        if tmp_d[j]=='X':
            X.append((i,j))
        elif tmp_d[j]=='T':
            T.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(graph,nx,ny,d):
    if nx>=0 and nx<n and ny>=0 and ny<n:
        if graph[nx][ny]=='O':
            return True
        elif graph[nx][ny]=='S':
            return False
        else:
            return dfs(graph,nx+dx[d],ny+dy[d],d)  #바보같은 실수...     
            
    else: 
        return True

Os=list(combinations(X,3))
for O in Os:
    answer=True
    for i in range(3):
        data[O[i][0]][O[i][1]]='O'
    
    for t in T:
        if answer==False:
            break
        nx=t[0]
        ny=t[1]
        for i in range(4):
            if dfs(data,nx+dx[i],ny+dy[i],i)==False:
                answer=False
                
    if answer:
        break

    for i in range(3):
        data[O[i][0]][O[i][1]]='X'

if answer:
    print('YES')
else:
    print('NO')

# 답지 안봄 (약 80분 소요)
# 전체적인 코드 구조는 짜기 쉬웠는데, 어이없는 오류를 저질렀다...
'''
오류: 
순환함수에서 X나 T를 만나면 계속 진행하면서 T/F를 만나면 해당 T/F를 return했어야 했는데, return없이 순환함수만 실행하게 했다.
따라서 T/F에 대한 정보를 넘겨주지 못해서 정확한 답을 얻지 못하게 되었다.
'''
# 문제해결 방법: 디버깅(노가다)