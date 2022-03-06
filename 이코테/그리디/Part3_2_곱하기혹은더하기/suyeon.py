import sys

#개행문자 제외 문자열 입력받기
num = sys.stdin.readline().strip()
result = 0 

#문자열 길이 만큼 반복
for i in range(len(num)): 
    if result==0 or (int(num[i]))==0 or (int(num[i]))==1: #처음숫자는 +, 만약 주어진 문자가 0이거나 1이면 기존 결과 +를 해준다. 
        result += int(num[i])
    else:
        result*=int(num[i]) #주어진 문자가 0,1이 아니면 곱해준다. 

print(result)
        
