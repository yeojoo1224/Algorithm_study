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

g=int(input())
p=int(input())

parent=[0]*(g+1)
for i in range(1,g+1):
    parent[i]=i

result=0
for _ in range(p):
    data=find_root(parent,int(input())) #현재 비행기의 찹승구의 루트 확인
    if data==0:
        break
    union(parent,data,data-1) #왼쪽 집합과 합치기
    result+=1

print(result)

#답지봄