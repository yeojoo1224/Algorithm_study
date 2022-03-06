#발상 메모: 정수의 길이를 구해서 길이의 반을 기준으로 양쪽 수의 합이 같도록 한다.

n = int(input())
ns = str(n)
length = len(ns)
count1=0
count2=0

for i in range(length):
    if(i>=0 and i<length//2):
        count1+=1
    else:
        count2+=1

if count1==count2:
    print("LUCKY")
else: print("READY")

