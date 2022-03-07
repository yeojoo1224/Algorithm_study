# 2차원 리스트 90도 회전
def rotate(key):
    a = len(key) # 행의 길이 
    b = len(key[0]) # 열의 길이
    key_rotate = [[0] * a for _ in range(b)] # 회전 후의 리스트
    for x in range(a):
        for y in range(b):
            key_rotate[y][a - x - 1] = key[x][y]
    return key_rotate

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(big_lock):
    lock_length = len(big_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if big_lock[i][j] != 1:
                return False  
    return True
  
def solution(key, lock):
    a = len(lock)
    b = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    big_lock = [[0] * (a * 3) for _ in range(a * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(a):
        for j in range(a):
            big_lock[i + a][j + a] = lock[i][j]
    
    # 4가지 방향에 대해 확인
    for rotation in range(4):
        key = rotate(key) # 열쇠 회전
        for x in range(a * 2):
            for y in range(a * 2):
                # 자물쇠에 열쇠 넣기
                for i in range(b):
                    for j in range(b):
                        big_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는 지 확인
                if check(big_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(b):
                    for j in range(b):
                        big_lock[x + i][y + j] -= key[i][j]
    
    return False
                
# key 리스트를 회전시키는 함수를 만든것까지는 잘 구현하였다
# 하지만 자물쇠의 크기를 기존의 3배로 변환하여 움직여야 한다는 생각을 하지못했다
# 또한 자물쇠의 중간 부분이 1인지 확인하는 부분을 따로 함수로 만드는 생각을 하지 못해 solution 부분에 넣으려 하다가 코드가 복잡해져서 실패했다