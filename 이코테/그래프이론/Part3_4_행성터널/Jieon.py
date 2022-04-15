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
"""
#n개의 행성 정보 받기
n=int(input())
planet=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    planet.append((x,y,z))

#행성간 거리를 구해서 저장
edges=[]
for i in range(n):
    ax,ay,az=planet[i]
    for j in range(n):
        bx,by,bz=planet[j]
        edges.append((min(abs(ax-bx),abs(ay-by),abs(az-bz)),i,j))
edges.sort()

#신장트리를 위한 parent
parent=[0]*n
for i in range(n):
    parent[i]=i

#최소신장트리 구하기
cost=0
for edge in edges:
    c,a,b=edge
    if find_root(parent,a)!=find_root(parent,b):
        cost+=c
        union(parent,a,b)

print(cost)
"""
#딥지안봄, 메모리초과 발생

#답지
n=int(input())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

x=[]
y=[]
z=[]

for i in range(1,n+1):
    data=list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

#인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n-1):
    #비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort()

#간선을 하나씩 확인
for edge in edges:
    cost,a,b=edge
    #사이클이 발생하지 않을 경우에만 집합에 포함
    if find_root(parent,a)!=find_root(parent,b):
        union(parent,a,b)
        result+=cost

print(result)
#머야... 이것도 시간초과 생김...뭐지?

