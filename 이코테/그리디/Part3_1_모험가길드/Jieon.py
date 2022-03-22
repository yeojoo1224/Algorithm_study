#가장 큰 공포도 개수만큼 그룹을 만들어 가는 방법.
'''
import sys

#데이터 받기
N=int(sys.stdin.readline())
fear=list(map(int,sys.stdin.readline().split()))
fear.sort() #데이터 정렬

result=0
index=-1 #공포도가 가장 높은것 부터 그룹화
while(index>=-N):
    index_fear=fear[index] #가장 큰 공포도
    result+=1 #(공포도 수 만큼)그룹화
    index-=index_fear #가장 큰 공포도 위치 변경
    
print(result)
'''

#복습
n=int(input())
data=sorted(list(map(int,input().split())))

cnt=0
group=0
for s in data:
    cnt+=1
    if cnt>=s:
        group+=1
        cnt=0
print(group)

#복습해보니 내가 예전에 풀었던 방법은 답이 안될 가능성이 큼. 문제에서 특정 모험가는 마을에 두어도 된다고 함.