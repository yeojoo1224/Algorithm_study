N=int(input())
data=list(map(int,input().split()))
dpt=[0]*(N)
dpt[0]=data[0]
dpt[1]=data[1]
for i in range(2,N): #i를 선택할 경우, 최대값 dpt에 저장
    dpt[i]=max(dpt[0:i-1])+data[i]

print(max(dpt))
#위의 방식은 N값이 작기 때문에 가능함. (N<=100)

#만약 N이 크다면? 그 전 식량창고 vs 한칸 떨어진 식량창고+현재 식량창고만 비교!
dpt[0]=data[0]
dpt[1]=max(data[0],data[1])
for i in range(2,N):
    dpt[i]=max(data[i-1],data[i-2]+data[i])

print(dpt[n-1])