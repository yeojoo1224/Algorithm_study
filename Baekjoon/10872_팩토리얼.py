#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())

def fac(n): #팩토리얼 함수 선언
    if n==0:
        return 1
    elif n<=2: #n이 2이하이면
        return n
    else: #n이 3이상이면 
        n = n * fac(n-1) #n = 4 -> 4*fac(3)-> 4*3*fac(2)-> 6->24
        return n

print(fac(n))