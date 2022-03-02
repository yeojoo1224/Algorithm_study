import sys

#개행문자 제외 문자열 입력받기
num = sys.stdin.readline().strip()
result = 0 

#문자열 길이 
for i in range(len(num)): 
    if result==0 or (int(num[i]))==0:
        result += int(num[i])
    else:
        result*=int(num[i])

print(result)
        