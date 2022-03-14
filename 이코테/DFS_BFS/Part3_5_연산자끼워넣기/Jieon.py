n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_v=1e9
max_v= -1e9

def dfs(i,now):
    global min_v,max_v,add,sub,mul,div
    if i==n:
        min_v=min(min_v,now)
        max_v=max(max_v,now)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1

        if div>0:
            div-=1
            if now>0:
                dfs(i+1,now//data[i])
            else:
                dfs(i+1,-(-now//data[i]))
            div+=1

dfs(1,data[0])
print(max_v)
print(min_v)

# 답지 완전 참고
# 10달전 풀었던 문제라니... 그런데 기억이 1도 안난다. 정말 꾸준히 공부하는게 답인 것 같다.
# 나에게 조금 너무 어려운 문제였다. 아직 재귀함수가 익숙하지 않은 것 같다. 재귀함수에 대한 감을 다른 문제를 풀어서 더 익혀야 할 것 같다.
# 눈에 보이는 그래프의 경우 dfs,bfs를 적용할 수 있는데 이런 문제 같은 상상으로 그래프를 그려야 하는 문제가 익숙하지 않다.