import sys
n = sys.stdin.readline().strip()
count =0

#이동 조합 딕셔너리 생성
move_types = [(-2,-1), (-2, 1), (-1,2), (-1,-2), (1,-2), (1,2), (2,-1), (2,1)]

for i in move_types:
    #각 이동 연산하기 전 행렬 초기화
    col = ord(n[0])
    row = int(n[1])

    col+=i[0]
    row+=i[1]
    #열과 행이 주어진 범위에서 넘치지 않을 때만 이동가능 경우의 수 count +1
    if (col>=97 and col<=104) and (row>=1 and row<=8):
        count+=1

print(count)



