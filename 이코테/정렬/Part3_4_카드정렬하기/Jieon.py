import heapq
N=int(input())
data=[]
for _ in range(N):
    heapq.heappush(data,int(input()))

answer=0

while len(data)!=1:
    n1=heapq.heappop(data)
    n2=heapq.heappop(data)
    tmp=n1+n2
    answer+=tmp
    heapq.heappush(data,tmp)

print(answer)

