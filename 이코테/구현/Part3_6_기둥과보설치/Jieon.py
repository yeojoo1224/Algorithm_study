def check(n,now_frame):
    for i in range(n):
        for j in range(n):
            if 1 in now_frame[i][j]: #교차점에 보가 있을 경우
                if (0 in now_frame[i-1][j]) or (0 in now_frame[i-1][j+1]) or ((1 in now_frame[i][j-1]) and (1 in now_frame[i][j+1])):
                    continue
                else: 
                    return False
            if 0 in now_frame[i][j]: #교차점에 기둥이 있을 경우
                if (i==0) or (1 in now_frame[i][j]) or (1 in now_frame[i][j-1]) or (0 in now_frame[i-1][j]):
                    continue
                else:
                    return False
    return True
                
def solution(n, build_frame):
    wall=[[[[2]] for _ in range(n+1)] for __ in range(n+1)]
    result=[]
    for frame in build_frame:
        if frame[3]==1: #frame 삽입
            wall[frame[1]][frame[0]].append(frame[2])
            result.append([frame[0],frame[1],frame[2]])
        else: #frame 삭제
            wall[frame[1]][frame[0]].remove(frame[2])
            result.remove([frame[0],frame[1],frame[2]])
            
        if check(n,wall)==False: #frame 삽입/삭제 오류시, 변화 반영 X
            if frame[3]==1:
                wall[frame[1]][frame[0]].remove(frame[2])
                result.remove([frame[0],frame[1],frame[2]])
            else:
                wall[frame[1]][frame[0]].append(frame[2])
                result.append([frame[0],frame[1],frame[2]])
    result.sort()
    return result

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))