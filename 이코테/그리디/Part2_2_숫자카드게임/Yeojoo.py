n, m = map(int, input().split())
result = 0

# card 리스트를 오름차순으로 정렬하여 가장 작은 수를 min_card에 저장
# min_card와 result를 비교하여 result를 더 큰 수로 대체해준다.
for i in range(n):
    card = list(map(int, input().split()))
    card.sort()
    min_card = card[0]

    result = max(result, min_card)

print(result)