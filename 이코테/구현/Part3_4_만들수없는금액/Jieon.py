import copy

def rotation(key,M):
    result=[[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            result[i][M-j-1]=key[j][i]
    return result

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

    ex_lock=[[0]*(3*N) for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            ex_lock[N+i][N+j]=lock[i][j]
    
    for _ in range(4):
        for i in range(2*N):
            for j in range(2*N):
                tmp_lock=copy.deepcopy(ex_lock) 
                for x in range(M):
                    for y in range(M):
                        tmp_lock[i+x][j+y]+=key[x][y]
                if check(tmp_lock,N):
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
                        tmp_lock[i+x][j+y]+=key[x][y]
                if check(tmp_lock,N):
                    return True
                for k in range(M):
                    for l in range(M):
                        tmp_lock[i+k][j+l]-=key[k][l]
        key=rotation(key,M)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))