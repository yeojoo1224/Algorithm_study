n = int(input())
# 모든 식량 정보 입력받기
house = list(map(int, input().split()))
# 앞서 계산된 모든 결과를 저장하기 위한 테이블 초기화
dp = [0] * 100

# 다이나믹 프로그래밍 진행(보텀업)
dp[0] = house[0]
dp[1] = max(house[0], house[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + house[i])

# 계산된 결과 출력
print(dp[n - 1])