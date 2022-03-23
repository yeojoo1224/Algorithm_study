import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(' '*(n-i) + '*' * (2*i-1))
#처음에는 range(1,2*n, 2)로 범위주고 center()써서 풀었는데(출력 결과는 같았음), 출력형식이 잘못됐다고 해서 바꿨다. 이 문제에서 원한것은 center방법이 아니었나보다~