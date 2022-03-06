#발상 노트: ord로 바꿔서 숫자, 문자일 때 나눠서 연산
s = list(input())

for i in range(len(s)):
    s[i] = ord(s[i])

#문자 저장해줄 리스트 생성
chrs = []
#합산한 숫자 저장하는 count
count=0

#숫자, 문자 경우 나누어서 합산
for i in range(len(s)):
    if s[i]>=48 and s[i]<=57:
        s[i] = int(chr(s[i]))
        count+=s[i]
    elif s[i]>=65 and s[i]<=96:
        chrs.append(chr(s[i])) #문자 저장할 배열에 문자 추가

#문자 오름차순 정렬이므로 sort해줌
chrs.sort()
print(chrs)
#합산한 숫자도 최종 배열 chrs 끝에 붙이기(string형태로 바꿔야지 나중에 공백없이 출력하는 join에서 에러 안남(;join은 string형태만 지원)
chrs.append(str(count))
result = "".join(chrs) #공백없이 chrs출력

print(result)