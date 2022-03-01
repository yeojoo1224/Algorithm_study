n, k = map(int, input().split())
count = 0

# n이 1이 아니면 반복 실행한다
while(n!=1):
    # n이 k로 나누어 떨어지면 n을 k로 나누고 count를 1 증가시킨다.
    if n%k == 0:
        n /= k
        count += 1
    # n이 k로 나누어 떨어지지 않으면 n에 n-1을 대입하고 count를 1 증가시킨다.
    else:
        n -= 1
        count += 1

print(count)