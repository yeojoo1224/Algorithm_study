N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = []

# dfs(재귀)를 이용하여 문제를 풀었다!
def dfs(res, i, add, sub, mul, div):
    global N
    # 연산자를 모두 사용했을 때 result 리스트에 값을 추가한다.
    if i == N:
        result.append(res)
    else:
        if add:
            dfs(res + A[i], i + 1, add - 1, sub, mul, div)
        if sub:
            dfs(res - A[i], i + 1, add, sub - 1, mul, div)
        if mul:
            dfs(res * A[i], i + 1, add, sub, mul - 1, div)
        if div:
            dfs(int(res / A[i]), i + 1, add, sub, mul, div - 1)

dfs(A[0], 1, add, sub, mul, div)

print(max(result))
print(min(result))

# 문제를 봤을때 모든 경우의 수를 재귀를 사용하여 리스트에 담아서 최대, 최소값을 찾아야겠다고 생각이 바로 났다.
