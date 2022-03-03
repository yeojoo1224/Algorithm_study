s = input()

# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우를 나누어서 설정
change0 = 0
change1 = 0

# 첫 숫자가 0일 경우 change1은 이미 1이 됨
if s[0] == 0:
    change1 = 1
# 첫 숫자가 1일 경우 change1은 이미 1이 됨
else:
    change0 = 1


for i in range(len(s)-1):
    # 앞의 숫자와 뒤의 숫자가 서로 다른 경우
    if s[i] != s[i+1]:
        # 뒷 숫자가 0일 때 change1은 하나 추가됨
        if s[i+1] == '0':
            change1 += 1
        # 뒷 숫자가 1일 때 change0은 하나 추가됨
        else:
            change0 += 1

# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중 더 적게 바꾼 쪽의 횟수를 출력한다
print(min(change0, change1))