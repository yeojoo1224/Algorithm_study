def bisect(a,s,e):
    mid=(s+e)//2
    if s>e:
        return False
    if a[mid]==mid:
        return mid
    elif a[mid]>mid:
        return bisect(a,s,mid-1)
    else:
        return bisect(a,mid+1,e)

n=int(input())
data=list(map(int,input().split()))

answer=bisect(data,0,n-1)
if answer:
    print(answer)
else:
    print(-1)

#답지안봄(30분)
#기존에 풀었던 탐색방법은 리스트에서 어떤 숫자의 위치를 파악하는 일차원적인 "탐색" 문제였지만,
#이런 문제같은 경우에, 탐색을 좀 더 차원을 높여 생각해야 할 것 같다. 재미있다.