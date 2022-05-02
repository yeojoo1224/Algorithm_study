# 1. N을 입력 받는다
n=int(input())
# 2. 모든 경우의 수를 셀 count 변수를 0으로 초기화 한다.
count=0
# 3. for문으 돌려서 시,분,초를 따진다. (3중 for문)
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            if '3' in str(h)+str(m)+str(s):
                count+=1
#     3-1) 시,분,초 안에 3이 포함되면 count 1 증가
# 4. count출력
print(count)

#nav: 여주 // driver: 지언