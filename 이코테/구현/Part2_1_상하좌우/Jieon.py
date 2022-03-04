#(답지안봄), 딕셔너리사용시 효과적

import sys
#read data
n=int(sys.stdin.readline())
plan=list(map(str,sys.stdin.readline().split()))

move={'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}

now=(1,1)
for i in plan:
    x=now[0]+move[i][0]
    y=now[1]+move[i][1]
    if (x>0 and x<=n) and (y>0 and y<=n):
        now=(x,y)

print(now[0],now[1])
