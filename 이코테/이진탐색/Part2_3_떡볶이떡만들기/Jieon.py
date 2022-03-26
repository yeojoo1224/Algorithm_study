import sys
def binary_search(r_lens,target,start,end):
    rc=0
    mid=(start+end)//2
    for l in r_lens:
        if l>mid:
            rc+=(l-mid)
    if rc==target:
        return mid
    elif rc>target:
        return binary_search(r_lens,target,mid+1,end)
    else:
        return binary_search(r_lens,target,start,mid-1)

n,m=map(int,input().split())
data=list(map(int,sys.stdin.readline().split()))

answer=binary_search(data,m,0,max(data))
if answer!=None:
    print(answer)

#답지참고
#모든 경우를 탐색할 생각을 하지 못했다.
#이진탐색을 정해진 리스트에서 탐색하는 경우 말고도, 이렇게 이론적으로 탐색해야 하는경우도 있다는 것을 알게 되었다.