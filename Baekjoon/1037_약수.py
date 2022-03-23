#양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
length = len(n_list)

n_list.sort() #오름차순 정렬

max_int = n_list[0] * n_list[-1] #최소공배수는 가장 작은 약수랑 가장 큰 약수랑 곱한 것

print(max_int)


