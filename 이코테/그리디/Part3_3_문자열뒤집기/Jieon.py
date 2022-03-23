'''
#가장 작은 뭉텅이 개수만큼 뒤집으면 된다. 0101101 -->3
import sys

S=str(sys.stdin.readline())

last=2 #가장 최근의 뭉탱이 숫자
cnt=[0,0] #배열로 만들었더니 정답코드보다 줄었음. cnt[0]:0 뭉탱이 개수 cnt[1]:1뭉탱이 개수

for i in range(len(S)-1):
    num=int(S[i])
    if last!=num: #가장 최근 뭉탱이 수랑 인덱스의 수가 다를 경우, 새로운 뭉탱이 시작
        cnt[num]+=1
    last=num #최근 뭉탱이 수 업데이트

print(min(cnt)) #가장 작은 뭉탱이 반복 회수 출력'''

s=str(input())
cnt=[0,0]
last=int(s[0])
cnt[last]+=1
for i in range(1,len(s)):
    if last!=int(s[i]):
        last=int(s[i])
        cnt[last]+=1

print(min(cnt))
