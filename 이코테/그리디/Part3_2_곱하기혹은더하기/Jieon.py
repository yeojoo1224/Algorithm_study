import sys

S=str(sys.stdin.readline())

result=int(S[0])
for i in range(1,len(S)-1):
    next=int(S[i])
    if result==0 or next==0: #둘 중 하나라도 0이면 덧셈 수행
        result+=int(S[i])
    else:
        result*=int(S[i])

print(result)