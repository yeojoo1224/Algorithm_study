n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()

count = 0

# 정렬된 볼링공 리스트의 원소들을 모두 확인한다
for i in range(n):
    # 리스트의 인덱스보다 뒤쪽 원소들과 비교한다.
    for j in range(i+1, n):
        # 해당 원소와 뒤쪽 인덱스의 원소가 다르면 count를 1 늘린다.
        if k[i] != k[j]:
            count += 1

print(count)

# 답지랑 완전 다르게 풀었는데 이렇게 풀어도 괜찮은지가 궁금하다
# 이것저것 입력을 넣어봤을 때는 다 맞았다 !