x=int(input())
dp_table=[0]*(x+1)
dp_table[2]=1
dp_table[3]=1
dp_table[5]=1

for i in range(4,x+1):
    can=[]
    if i%5==0:
        can.append(dp_table[i//5])
    if i%3==0:
        can.append(dp_table[i//3])
    if i%2==0:
        can.append(dp_table[i//2])
    can.append(dp_table[i-1])

    dp_table[i]=min(can)+1

print(dp_table[x])

#답지안봄.