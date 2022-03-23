n=int(input())
cnt=0
coins=[500,100,50,10]
for coin in coins:
    if n>=coin:
        cnt+=n//coin
        n-=coin*(n//coin)
    if n==0:
        break

print(cnt)