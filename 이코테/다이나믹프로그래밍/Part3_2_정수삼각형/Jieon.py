n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    for j in range(i+1):
        data[i][j]+=max(data[i+1][j],data[i+1][j+1])

print(data[0][0])

#답지안봄
#bottom-up으로 풀기 쉬웠던 문제.