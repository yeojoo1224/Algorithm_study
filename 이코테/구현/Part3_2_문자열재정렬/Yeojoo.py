from curses.ascii import isalpha


s = input()
# 문자만을 담을 리스트를 정의
alpha = []
# 숫자들을 더할 count 변수를 0으로 초기화
count = 0

for i in range(int(len(s))):
    # s[i]의 원소가 알파벳인 경우를 isalpha를 이용해 찾는다
    if s[i].isalpha():
        # alpha 리스트에 알파벳을 담는다
        alpha.append(s[i])
    # s[i]의 원소가 알파벳이 아닌 정수인 경우 숫자를 모두 더한다
    else:
        count += int(s[i])

# 알파벳이 든 리스트를 sort() 함수를 이용하여 알파벳 순으로 정렬한다.
alpha.sort()
# 정렬된 알파벳 리스트의 맨 뒤에 숫자의 합산 값을 append한다.
alpha.append(str(count))

# join()함수를 이용하여 리스트 값을 띄어쓰기 없이 이어서 출력한다.
print(''.join(alpha))


# 알파벳만을 따로 받아오기 위한 isalpha와, 리스트를 띄어쓰기 없이 출력하기 위한 join()은 인터넷 검색을 통해 알아와서 코드를 작성했다.
# join 함수는 문자로 이루어진 리스트에만 쓸 수 있어서 count를 str타입으로 append 해주었다.
# 이런 문제들도 계속 풀다보면 검색을 하지 않고도 바로바로 풀수있겠지!!