#(답지안봄)구현 말고 그리디로 풀었음
import sys
N=int(sys.stdin.readline())

#N시 전에 3이 포함된 시간 개수 세기
n=0
three_hour=[3,13,23]
for i in three_hour:
    if N>=i:
        n+=1

h3=n*60*60 #시에 3이 포함된 경우

#시에 3이 포함되지 않고, 분or초에 3이 포함된 경우
ms3=0
for m in range(0,60):
    for s in range(0,60):
        if '3' in str(m)+str(s):
            ms3+=1
ms3*=(N-n+1)

print(h3+ms3)