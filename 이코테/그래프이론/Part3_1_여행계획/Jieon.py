def find_root(parent,x):
    if parent[x]!=x:
        parent[x]=find_root(parent,parent[x])
    
    return parent[x]

def union(parent,a,b):
    pa=find_root(parent,a)
    pb=find_root(parent,b)
    if pa>pb:
        parent[pa]=pb
    else:
        parent[pb]=pa

n,m=map(int,input().split())
parent=[0]*n
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(i+1,n):
        if l[j]==1:
            union(parent,i,j)
        
t_spot=list(map(int,input().split()))
group=parent[t_spot[0]-1]
flag=True
for s in t_spot:
    if group!=parent[s-1]:
        flag=False

if flag:
    print('Yes')
else:
    print('No')