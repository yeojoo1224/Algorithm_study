import bisect
n,x=map(int,input().split())
data=list(map(int,input().split()))
l=bisect.bisect_left(data,x)
r=bisect.bisect_right(data,x)
if r-l:
    print(r-l)
else:
    print(-1)

#답지안봄.(10분)
#bisect 라이브러리를 사용하면 훨씬 빠름. O(logN)

