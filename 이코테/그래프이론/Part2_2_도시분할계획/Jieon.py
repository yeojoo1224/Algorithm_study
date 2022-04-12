#최소신장트리 문제
def find_root(parents,a):
    if parents[a]!=a:
        parents[a]=find_root(parents, parents[a])
    return parents[a]

def union(parents,a,b):
    ra=find_root(parents,a) #이 부분 실수하지 말기!!!
    rb=find_root(parents,b)
    if ra>rb:
        parents[ra]=rb
    else:
        parents[rb]=ra

n,m=map(int,input().split())
parents=[0]*(n+1)
for i in range(n+1):
    parents[i]=i

edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()
last=0 #가장 큰 간선, 2개의 신장트리를 만들기 위함
cost=0
for edge in edges:
    c,a,b=edge
    if find_root(parents,a) != find_root(parents,b):
        union(parents,a,b)
        cost+=c
        last=c

print(cost-last)

#답지 일부 참조