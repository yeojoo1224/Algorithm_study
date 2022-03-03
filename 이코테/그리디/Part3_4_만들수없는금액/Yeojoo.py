n = int(input())
coin = list(map(int, input().split()))
# 동전들 모임을 오름차순으로 정렬
coin.sort()

money = 1

for i in coin:
    # 만들 수 없는 금액이 되면 반복문 종료
    if i > money:
        break
    # 다음 코인을 더해도 만들 수 있는지 반복
    else:
        money += i

print(money)