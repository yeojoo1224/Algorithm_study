n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_pay = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = i + t[i]
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_pay)
        max_pay = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_pay

print(max_pay)