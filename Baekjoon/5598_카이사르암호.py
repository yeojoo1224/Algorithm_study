#입력은 한 줄로 이루어져 있으며, 그 한 줄에는 대문자 알파벳으로 구성된 단어가 1개 있다. 단어는 최대 1000자 이하이다.
import sys
s = list(sys.stdin.readline().strip()) #l
length = len(s)

for i in range(length):
    if s[i] == 'A' or s[i]=='B' or s[i] == 'C':
        s[i]= ord(s[i]) + 23
    else: 
        s[i]= ord(s[i]) -3
    s[i] = chr(s[i])

result_s= ''.join(s)
print(result_s)



