# 1. n과 m을 입력받는다
n, m = map(int, input().split())
max_v = 0
# 2. n번 반복
for i in range(n):
    max_v = max(max_v,min(list(map(int, input().split()))))
#   2-1. 카드 행 입력, 그 중 가장 작은 값만 데이터에 저장
#3. 데이터에서 가장 큰 값 출력
print(max_v)