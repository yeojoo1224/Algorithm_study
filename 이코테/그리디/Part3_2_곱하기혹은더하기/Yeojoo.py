# 문자열 입력 받기
s = input()
# 첫 숫자를 result로 설정
result = int(s[0])

for i in range(1, len(s)):
    # result: 더하거나 곱해지는 앞 숫자
    # int(s[i]): 더하거나 곱해지는 뒷 숫자
    # result나 int(s[i])가 0이거나 1이면 곱하는 것보다 더하는 것이 큰 숫자를 만들기 유리
    if result <= 1 or int(s[i]) <= 1:
        result += int(s[i])
        
    # result나 int(s[i])가 0이나 1이 아니면 곱하는 것이 큰 숫자를 만들기 유리
    else:
        result *= int(s[i])

print(result)