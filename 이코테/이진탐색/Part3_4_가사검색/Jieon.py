from bisect import bisect_left, bisect_right
def cnt_by_range(data,s,e):
    left=bisect_left(data,s)
    right=bisect_right(data,e)
    return right-left

def solution(words, queries):
    answer = []
    #단어 길이별로 분류
    word_len=[[] for _ in range(10001)]
    r_word_len=[[] for _ in range(10001)]
    for w in words:
        word_len[len(w)].append(w)
        r_word_len[len(w)].append(w[::-1])
    
    #길이별 단어 정렬 (구간별 개수를 구하기 위함)
    for i in range(10001):
        word_len[i].sort()
        r_word_len[i].sort()
    
    for q in queries:
        if q[0]!='?':
            cnt=cnt_by_range(word_len[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            q=q[::-1]
            cnt=cnt_by_range(r_word_len[len(q)],q.replace('?','a'),q.replace('?','z'))

        answer.append(cnt)
    
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))