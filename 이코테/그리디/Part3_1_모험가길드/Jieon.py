#가장 큰 공포도 개수만큼 그룹을 만들어 가는 방법.
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
