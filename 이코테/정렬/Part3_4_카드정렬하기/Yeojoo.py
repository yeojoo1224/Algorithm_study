import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
cards = []
for i in range(n):
    card = int(input())
    heapq.heappush(cards, card)

result = 0

# 힙에 원소가 1개 남을 때까지
while len(cards) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    min1 = heapq.heappop(cards)
    min2 = heapq.heappop(cards)

    # 카드 묶음을 합쳐서 다시 삽입
    sum = min1 + min2
    result += sum
    heapq.heappush(cards, sum)

print(result)