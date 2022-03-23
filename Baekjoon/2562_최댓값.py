#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
import sys
count = 0
max_int = 0
max_idx = 0

for i in range(1, 10):
    n = int(sys.stdin.readline()) #숫자입력

    if max_int<n: #최댓값이 n보다 작으면
        max_int = n #n이 최댓값이 됨
        max_idx = i #그때의 i가 최댓값의 인덱스가 됨

print(max_int)
print(max_idx)

    