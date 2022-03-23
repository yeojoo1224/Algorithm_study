#첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
import sys
n = int(sys.stdin.readline())

for i in range(n, 0, -1): #n부터 1까지 별의 개수 차례대로 출력
    print('*'*i)