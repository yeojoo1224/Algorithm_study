s= input()

count0 = 0 #다 0으로 바꾸는 횟수
count1 = 0 #다 1로 바꾸는 횟수

#처음부터 뒤집고 시작하는 경우는 각 경우에 +1
if s[0]=='0':
    count1+=1
else:
    count0+=1

#길이보다 하나 더 작을때까지 비교
for i in range(len(s)-1): 
    if s[i]!=s[i+1]: #이웃한 수가 다를 때
        if s[i+1]=='0': #다음 수가 0이면 1로 바꿔야 하는 횟수를 하나 증가
            count1+=1
        else: #다음수가 1이면 0으로 바꾸는 횟수 하나 증가
            count0+=1

print(min(count0,count1)) #전체를 다 0으로 바꾸는 횟수와 1로 바꾸는 횟수 중 작은 수를 출력

