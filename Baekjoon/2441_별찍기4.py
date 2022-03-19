#첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
import sys
n = int(sys.stdin.readline())

for i in range(n,0,-1):
    star = '*' * i #별찍기 i개(n개부터 1개까지)
    print(star.rjust(n)) #i개 별찍은걸 오른쪽으로 정렬