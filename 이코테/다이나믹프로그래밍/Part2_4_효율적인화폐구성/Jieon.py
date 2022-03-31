n,m=map(int,input().split())
coins=[]
data=[0]*(10001)
for i in range(n):
    coin=int(input())
    coins.append(coin)
    data[coin]=1

for i in range(1,m+1):
    if data[i]!=0:
        continue
    min_v=m+1
    for c in coins:
        if i-c>0 and data[i-c]>0:
            min_v=min(min_v,data[i-c]+1)
    if min_v!=m+1:
        data[i]=min_v

#정답 출력
if data[m]==0:
    print(-1)
else:
    print(data[m])

#답지안봄.
#답지랑 풀이방식 비슷.