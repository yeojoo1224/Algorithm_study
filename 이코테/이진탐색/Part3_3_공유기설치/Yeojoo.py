n, c = map(int, input().split()) 

x = []
for _ in range(n):
    x.append(int(input()))
x.sort()

start = 1 # 최소 거리
end = x[-1] - x[0] # 최대 거리
dis = 0 

def binary(x, start, end):
    while start <= end:
        mid = (start + end) // 2 # 두 공유기 사이의 거리(gap)
        current = x[0]
        count = 1

        for i in range(1, n):
            if x[i] >= current + mid:
                count += 1
                current = x[i]
        
        if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
            global dis
            start = mid + 1
            dis = mid # 최적의 결과를 저장
        else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
            end = mid - 1

binary(x, start, end)
print(dis)