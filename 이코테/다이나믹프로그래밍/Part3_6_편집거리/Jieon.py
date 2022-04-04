#일단 골드만삭스라니... 뉴스에서만 들어본 그 이름...ㅎ
#이 문제 학교 알고리즘 수업에서 과제로 했던 기억이...
a=str(input())
b=str(input())
dpt=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(len(b)+1):
    dpt[0][i]=i
for j in range(len(a)+1):
    dpt[j][0]=j

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dpt[i][j]=dpt[i-1][j-1]
        else:
            dpt[i][j]=1+min(dpt[i][j-1],dpt[i-1][j],dpt[i-1][j-1]) #삽입,삭제,교체 중 최소비용 찾아 선택

print(dpt[len(a)][len(b)])

#답지참고