#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    star = 2*i-1
    print(' '*(n-i)+ '*' * (star))
    if star==2*n-1: #star가 2n-1까지 오름차순 개수로 다 출력되면
        for i in range(1,n+1):
            print(' '*i + '*' *(2*(n-i)-1)) #역순으로 출력


#ver 2
#import sys
#n = int(sys.stdin.readline())

#for i in range(1,n+1):
    #print(' '*(n-i)+ '*' * (2*i-1))
#for i in range(1,n+1):
#   print(' '*i + '*' *(2*(n-i)-1)) #역순으로 출력
