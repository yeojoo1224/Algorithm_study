def find_root(parent,x):
    if parent[x]!=x:
        parent[x]=find_root(parent,parent[x])
    
    return parent[x]

def union(parent,a,b):
    ra=find_root(parent,a)
    rb=find_root(parent,b)
    if ra>rb:
        parent[ra]=rb
    else:
        parent[rb]=ra
    
n,m=map(int,input().split())
parent=[0]*n
for i in range(n):
    parent[i]=i

edges=[]
total_cost=0
for i in range(m):
    a,b,c=map(int,input().split())
    total_cost+=c
    edges.append((c,a,b))

edges.sort()

active_cost=0
for edge in edges:
    z,x,y=edge
    if find_root(parent,x)!=find_root(parent,y):
        union(parent,x,y)
        active_cost+=z

print(total_cost-active_cost)

#답지 안봄
