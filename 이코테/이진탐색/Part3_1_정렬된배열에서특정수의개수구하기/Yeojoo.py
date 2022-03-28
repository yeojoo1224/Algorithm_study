from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

left = bisect_left(array, x)
right = bisect_right(array, x)

if right - left:
    print(right - left)
else:
    print(-1)