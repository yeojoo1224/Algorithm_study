n = int(input())
count = 0

#h, m, s의 범위를 설정하여 for문 작성
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            #h, m, s를 str타입으로 생각하여 각 자리수에 3이 하나라도 있으면 count를 1 증가
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count += 1
            
print(count)

#해설을 참조하고 9열의 if문을
# if '3' in str(h) + str(m) + str(s)로 바꾸는게 더 간결하다는 것을 느꼈다.