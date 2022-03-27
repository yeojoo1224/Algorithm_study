n = int(input())
n_device = list(map(int, input().split()))
n_device.sort()

m = int(input())
m_device = list(map(int, input().split()))

# 이진탐색 코드
def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end =  mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return False

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in m_device:
    # 해당 부품이 존재하는지 확인
    if binary(n_device, i, 0, n - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')