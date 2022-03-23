#7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
import sys
result = 0
min_int = 100

for i in range(7):
    n = int(sys.stdin.readline()) #숫자 입력
    if n%2==0: #짝수면 패스
        continue 
    else: #홀수면 결과값에 그 수를 더하고, 최솟값을 비교한다. 
        result += n 
        if min_int>n:
            min_int=n

if result==0:
    print(-1)
else:
    print(result)
    print(min_int)

