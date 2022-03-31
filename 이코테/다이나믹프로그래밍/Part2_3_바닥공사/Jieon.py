n=int(input())
dpt=[0]*(n+1)
dpt[0]=0
dpt[1]=1
dpt[2]=3
for i in range(3,n+1):
    dpt[i]=(dpt[i-1]+dpt[i-2]*2)%796796

print(dpt[n])
#답지참조