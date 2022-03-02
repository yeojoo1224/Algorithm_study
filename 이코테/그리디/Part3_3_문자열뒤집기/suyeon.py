line = [int(i) for i in list(input())]
result = 0
count0 = 0 #0으로 바뀌는 횟수
count1 = 0 #1로 바뀌는 횟수

if line[0]: #시작이 1이면
    count0 += 1 #0으로 바뀜
else:
    count1 += 1

for i in range(len(line)-1):
    if line[i] != line[i+1]: #다르면
        if line[i+1]: #0->1
            count0 += 1
        else: #1->0
            count1 += 1
    #print(count0, count1)
result = min(count1, count0)

print(result)




