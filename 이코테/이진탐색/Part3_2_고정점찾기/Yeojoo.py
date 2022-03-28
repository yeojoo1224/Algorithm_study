n = int(input())
array = list(map(int, input().split()))
 
def binary(array, start, end):
    if start > end:
        return False
    # 중간 지점을 설정
    mid = (start + end) // 2
    # 인덱스와 원소 값이 같다면 해당 점을 return
    if mid == array[mid]:
        return mid
    # 원소 값보다 인덱스가 작다면, 해당 인덱스의 왼쪽 부분에 고정점이 있으므로 재귀 사용
    elif mid < array[mid]:
        return binary(array, start, mid - 1)
    # 원소 값보다 인덱스가 크다면, 해당 인덱스의 오른쪽 부분에 고정점이 있으므로 재귀 사용
    else:
        return binary(array, mid + 1, end)

search = binary(array, 0, n - 1)

if search:
    print(search)
else:
    print(-1)