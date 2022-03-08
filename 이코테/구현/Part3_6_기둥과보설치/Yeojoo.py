# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def can_build(answer):
    for x, y, line in answer:
        if line == 0: # 설치한 선이 기둥인 경우
            # '바닥 위', '보의 한쪽 끝부분 위', '다른 기둥 위'라면 정상
            if y == 0 or [x- 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓 반환
        elif line == 1: # 설치한 선이 보인 경우
            # '한쪽 끝부분이 기둥 위', '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓 반환
    return True   
    

def solution(n, build_frame):
    answer = []
    for work in build_frame: # 작업(work)의 개수는 최대 1000개
        x, y, line, step = work
        if step == 0: # 삭제하는 경우
            answer.remove([x, y, line]) # 일단 삭제를 해본 뒤에
            if not can_build(answer): # 가능한 구조물인지 확인
                answer.append([x, y, line]) # 가능한 구조물이 아니라면 다시 설치 
        if step == 1: # 설치하는 경우
            answer.append([x, y, line]) # 일단 설치를 해본 뒤에
            if not can_build(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, line]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환

# 답지 참조 하지 않고 잘 작성한 후에 답지를 참조 후 다시 깔끔하게 정리했다!
# 설치한 선이 기둥 혹은 보일 경우 가능한 구조물인지 if문 작성하는게 좀 복잡해서 오래걸렸댜