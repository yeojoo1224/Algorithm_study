n = int(input())
dp = [1] * n

sol = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        # 내림차순이면
        if sol[i] < sol[j]:
            dp[i] = max(dp[i], dp[j] + 1)        
# max(dp)는 가장 긴 내림차순 부분 수열의 길이
print(n - max(dp))