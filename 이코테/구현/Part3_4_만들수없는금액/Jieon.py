#(답지참조)
import copy
#키 회전 (90도 시계방향)
def rotation(key,M):
    result=[[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            result[i][M-j-1]=key[j][i]
    return result

#자물쇠가 풀리는지 확인
def check(n_lock,N):
    for i in range(N,2*N):
        for j in range(N,2*N):
            if n_lock[i][j]!=1:
                return False
    return True

#key 이동마다 deepcopy시전 --> 느림
def solution(key, lock):
    M=len(key)
    N=len(lock)

    #3배 확장
    ex_lock=[[0]*(3*N) for _ in range(3*N)]
    #확장 자물쇠 중간에 실제 자물쇠 저장
    for i in range(N):
        for j in range(N):
            ex_lock[N+i][N+j]=lock[i][j]
    
    for _ in range(4):
        for i in range(2*N):
            for j in range(2*N):
                tmp_lock=copy.deepcopy(ex_lock) #key이동마다 원래 자물쇠로 초기화
                for x in range(M):
                    for y in range(M):
                        tmp_lock[i+x][j+y]+=key[x][y] 
                if check(tmp_lock,N): #풀리는지 확인
                    return True
        key=rotation(key,M)
    return False

#key이동하기 전에 lock에 더한 key삭제 (deepcopy X) --> 훨씬 빠름
def solution2(key,lock):
    M=len(key)
    N=len(lock)

    tmp_lock=[[0]*(3*N) for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            tmp_lock[N+i][N+j]=lock[i][j]
    
    for _ in range(4):
        for i in range(2*N):
            for j in range(2*N):
                for x in range(M):
                    for y in range(M):
                        tmp_lock[i+x][j+y]+=key[x][y] #lock+key==1 이면 열림
                if check(tmp_lock,N): #열리는지 확인 
                    return True
                for k in range(M): #자물쇠 원래대로 초기화 
                    for l in range(M):
                        tmp_lock[i+k][j+l]-=key[k][l]
        key=rotation(key,M)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))