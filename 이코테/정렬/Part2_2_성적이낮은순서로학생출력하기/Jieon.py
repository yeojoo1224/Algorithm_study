n=int(input())
list=[0]*(101)
for _ in range(n):
    name,score=map(str,input().split())
    list[int(score)]=name

for i in range(101):
    if list[i]!=0:
        print(list[i],end=' ')

#계수정렬로 풀기 좋은 문제.