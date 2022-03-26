#data 받기
import sys
print("n")
n=int(input())
print("n개의 부품")
n_list=sorted(list(map(int,sys.stdin.readline().split())))
print("m")
m=int(input())
m_list=list(map(int,sys.stdin.readline().split()))

#이진탐색 함수
def binary_search(array,target,start,end):
    mid=(start+end)//2
    if start>end:
        return False
    else:
        if array[mid]==target:
            return True
        elif array[mid]>target:
            return binary_search(array,target,start,mid-1)
        else:
            return binary_search(array,target,mid+1,end)

#이진탐색
answer=[]
for i in range(m):
    if binary_search(n_list,m_list[i],0,n-1):
        answer.append('yes')
    else:
        answer.append('no')

for i in answer:
    print(i,end=' ')

#답지안봄. 탐색 재밌다.