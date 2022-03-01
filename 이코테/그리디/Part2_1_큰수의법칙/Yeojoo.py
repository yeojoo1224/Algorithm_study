n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# sort를 이용하여 arr 리스트를 오름차순으로 정렬
arr.sort()

# a와 b는 각각 가장 큰 수, 두번째로 큰 수
a = arr[-1]
b = arr[-2]

# 가장 큰 수는 m//k회씩 k번 더해주고
# 두번째로 큰 수는 전체에서 가장큰 수를 더한 횟수를 뺀 만큼 더해준다.
result = a*k*(m//k) + b*(m-k*(m//k))

print(result)