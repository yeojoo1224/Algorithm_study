from itertools import combinations

n,m = map(int, input().split())
chicken, house = []

for r in range(n):
    city = list(map(int, input().split()))
    for c in range(n):
        if city[c] ==1:
            house.append((r,c)) #일반 집 좌표 추가 
        elif city[c] ==2:
            chicken.append((r,c)) #치킨 집 좌표 추가
#좌표를 이렇게 한꺼번에 입력받을 수 있는지도 몰랐네.. 문법 공부 해야겠다..
    
#모든 치킨 집 중에서 m개의 치킨집을 뽑는 모든 '조합'계산_ 조합기능도 처음 본다
candidates= list(combinations(chicken,m))

#치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    #모든 집에 대해
    for hx, hy in house:
        #가장 가까운 치킨집을 찾기
        temp = 1e9#엄청 큰 수
        for cx,cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        #가장 가까운 치킨집까지의 거리를 더하기
        result +=temp
#치킨 거리의 값 반환
    return result

#치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
            
print(result)



