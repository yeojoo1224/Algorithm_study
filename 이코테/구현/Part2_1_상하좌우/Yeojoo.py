n = int(input())
arr = list(map(str, input().split()))
#시작 위치 초기화
a, b = 1, 1

#c, d를 이용하여 초기 위치를 옮겨다님
for i in arr:
    #l(left)이면 c는 a위치, d는 b-1 위치
    if i == 'l':
        c = a
        d = b - 1
    elif i == 'r':
        c = a
        d = b + 1
    elif i == 'u':
        c = a - 1
        d = b
    else:
        c = a + 1
        d = b
    
    #옮긴 c, d위치가 정사각형 공간 밖이면 최종 이동한 a, b위치를 이동하지 않는다.
    if c < 1 or d < 1 or c > n or d > n:
        continue

    a, b = c, d

print(a, b)


#문제 해설을 본 후 l,r,u,d도 리스트화 하여 구현하면 코드가 더 깔끔해졌을 것이라 느꼈다.