import sys
S=list(str(sys.stdin.readline())) #string to list

result=[]
num=0
for i in range(len(S)-1):
    if '0'<=S[i] and '9'>=S[i]: #숫자인 경우
        num+=int(S[i])
    else:
        result.append(S[i]) #문자인 경우

result.sort() #문자 오름차순 정렬 
result.append(str(num)) #합 추가
print("".join(result)) #list to string
