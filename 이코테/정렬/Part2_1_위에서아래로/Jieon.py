N=int(input())
list=[]
for i in range(N):
    list.append(int(input()))
list.sort(reverse=True)

for i in list:
    print(i,end=' ')