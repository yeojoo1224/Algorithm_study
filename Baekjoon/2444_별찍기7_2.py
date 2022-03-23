<<<<<<< HEAD
#ver 2 그냥 단순하게 
import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(' '*(n-i)+ '*' * (2*i-1))
for i in range(1,n+1):
=======
#ver 2 그냥 단순하게 
import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(' '*(n-i)+ '*' * (2*i-1))
for i in range(1,n+1):
>>>>>>> 46ef02aff5789a72439ba502bc3fb0d29d59a548
    print(' '*i + '*' *(2*(n-i)-1)) #역순으로 출력