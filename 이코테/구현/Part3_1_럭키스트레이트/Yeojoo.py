n = input()
# 문자열의 왼쪽 부분의 합을 0으로 초기화한다
left_n = 0
# 문자열의 오른쪽 부분의 합을 0으로 초기화한다
right_n = 0
# 문자열의 크기를 length로 명시
length = int(len(n))

# 문자열의 왼쪽 부분의 자릿수의 합을 구한다.
for i in range(int(length/2)):
    left_n += int(n[i])

# 문자열의 오른쪽 부분의 자릿수의 합을 구한다.
for i in range(int(length/2), length):
    right_n += int(n[i])

# 문자열의 왼쪽 부분과 오른쪽 부분의 합이 같은 경우와 다른 경우 상태를 출력한다
if left_n == right_n:
    print("LUCKY")

else:
    print("READY")