
# 1. N과 K를 입력받는다.
n,k=map(int,input().split())
# 2. cnt=0 초기화
cnt=0
'''
# 3. while문 실행 (n>=k)
while n>=k:
# 3-1. while문 실행 (n%k!=0): n-1 // cnt+=1
    while n%k!=0:
        n-=1
        cnt+=1
# 3-2. n/=k // cnt+1
    n/=k
    cnt+=1
# 4. while (n>1):
while(n>1):
# 4-1. n-=1 // cnt+=1
    n-=1
    cnt+=1
# # 5. cnt 출력
print(cnt)
'''

# 3. while 문 실행 (n>1)
while n>1:
# 3-1. r=n%k n=(n-r)/k cnt+=r+1
    if n<k:
        cnt+=n-1
        break
    r=n%k
    n=(n-r)//k
    cnt+=r+1
    

print(cnt)