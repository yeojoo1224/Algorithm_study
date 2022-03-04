#sys가 시간 더 적게 걸리므로 얘 사용
import sys
n = int(sys.stdin.readline())

#공백길이까지 포함하지 않도록 strip 사용
road = sys.stdin.readline().strip().split()
length = len(road)
x = 1
y = 1

#좌표가 1과 n사이에 존재할 때만 이동이 가능하도록 조건 나누어 구현
for i in range(length):
    if road[i] =="U" and x!=1:
        x-=1
    elif road[i]=="D" and x!=n:
        x+=1
    elif road[i]=="L" and y!=1:
        y-=1
    elif road[i]=="R" and y!=n:
        y+=1
    
print("%d %d"%(x,y))

