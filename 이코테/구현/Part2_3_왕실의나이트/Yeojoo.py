# 나이트의 위치를 리스트로 받는다
loc = list(input())
# 열 위치를 ord를 이용하여 숫자로 표현한다.
col = int(ord(loc[0]))
row = int(loc[1])

# 이동 가능한 경우의 수를 count로 나타내어 0으로 초기화
count = 0
# 앞선 상하좌우의 해설처럼 이동 가능한 경우를 move라는 리스트로 표현
move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)]

for i in move:
    # dir1을 이동한 열, dir2를 이동한 행으로 표시
    dir1 = col + i[0]
    dir2 = row + i[1]

    # 아스키 코드를 숫자로 나타냈을 때 'a' = 97, 'h' = 104
    # 이동한 위치가 체스판을 벗어났을 때 continue를 통해 count의 증가를 막는다.
    if dir1 > 104 or dir2 > 8 or dir1 < 97 or dir2 < 1:
        continue
    count += 1

print(count)

# 해설에서는 ord를 사용하는것은 같았으나
# int(ord(input_data[0])) - int(ord('a')) + 1로 코드를 구현하여 알아보기 쉽게 나타냈다.