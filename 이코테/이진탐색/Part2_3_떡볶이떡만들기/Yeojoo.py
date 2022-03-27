n, m = map(int, input().split())
h = list(map(int, input().split()))

# 시작점과 끝점 설정
start = 0
end = max(h)

result = 0

# 이진 탐색 수행
while(start <= end):
    ddeok = 0
    mid = (start + end) // 2

    for i in h:
        # 잘랐을 때 떡의 양 계산
        if i > mid:
            ddeok += i - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if ddeok < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start = mid + 1
    
print(result)