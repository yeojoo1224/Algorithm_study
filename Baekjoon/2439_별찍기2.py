import sys
n= int(sys.stdin.readline())

for i in range(1,n+1):
    star = '*' * i
    print(star.rjust(n))
#꼭 반복문 2개 써야된다는 생각 버리기!
