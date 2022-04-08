#서로소 집합 문제
def find_root(parent,a):
    if parent[a]!=a:
        parent[a]=find_root(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    pa=find_root(parent,a)
    pb=find_root(parent,b)
    if pa==pb:
        return
    elif pa>pb:
        parent[pa]=pb
    else:
        parent[pb]=pa

n,m=map(int,input().split())

parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i

result=[]
for _ in range(m):
    method,a,b=map(int,input().split())
    if method==0:
        union(parent,a,b)
    else:
        ra=find_root(parent,a)
        rb=find_root(parent,b)
        if ra==rb:
            result.append('YES')
        else:
            result.append('NO')

for answer in result:
    print(answer)

#답지안봄