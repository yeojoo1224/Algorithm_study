# 답지봄... 조합쓸 생각을 못함. 보바
from itertools import combinations
import sys

from numpy import Inf
n,m=map(int,sys.stdin.readline().split())
c_map=[]
for _ in range(n):
    c_map.append(list(map(int,sys.stdin.readline().split())))

chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if c_map[i][j]==1:
            house.append([i,j])
        if c_map[i][j]==2:
            chicken.append([i,j])

candidates=list(combinations(chicken,m)) #치킨집중 M개 선택 (조합)

def get_citycd(r_chicken): #남은 M개의 치킨집에 대한 도시치킨거리 구하기
    citycd=0
    for hx,hy in house:
        temp=1e9
        for cx, cy in r_chicken:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        citycd+=temp
    return citycd

result=1e9
for r_chicken in candidates:
    result=min(result,get_citycd(r_chicken))

print(result)
