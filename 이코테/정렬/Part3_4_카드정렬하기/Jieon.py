from collections import deque
N=int(input())
data=[]
for _ in range(N):
    data.append(int(input()))

answer=0
while len(data)>1:
    data.sort()
    tmp=[]
    for i in range(1,len(data),2):
        answer+=data[i]+data[i-1]
        tmp.append(data[i]+data[i-1])
    if len(data)%2!=0:
        tmp.append(data[-1])
    data=tmp

print(answer)
