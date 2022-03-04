n = int(input())

#3이 하나라도 포함되어있는 거 구하기 = 전체 경우의 수 - 3이 하나도 없는 수
result = 45*45 #3이 포함된 분과 초= 15개 제외하면 45*45개가 3이 하나도 없는 분,초 세트이다. 
origin = (n+1)*60*60 #전체 경우의 수

#13을 기준으로 3이 포함되지 않은 n의 개수가 달라지므로 나누어서 계산    
if n>=0 and n<13:
     result*=(n)
elif n>=13 and n<23:
    result*=(n-1)

result = origin - result


print(result)

