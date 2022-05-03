# 1. 나이트가 이동할 수 있는 경우의 수 튜플 리스트 만들기 
move_l = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 2. 첫번째 위치 입력
first_loc = str(input())
# 3. 입력받은 위치를 (x, y)로 나타내기
x = int(first_loc[1])
y = int(ord(first_loc[0]) - ord('a')) + 1
count = 0
# 4. 8번 반복 (나이트가 이동할 수 있는 경로 모두 비교)
for move in move_l:
    # 4-1. 1에서받은 튜플 리스트 중 하나를 뽑아와 체스판 안에 있는 지 확인
    nx = x + move[0]
    ny = y + move[1]
    # 4-2. 가능하면 count += 1
    if 0 < nx < 9 and 0 < ny < 9:
        count += 1 
# 5. count 출력
print(count)


#nav: 지언 // driver: 여주