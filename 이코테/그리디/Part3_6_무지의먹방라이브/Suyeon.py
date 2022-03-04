
def solution(food_times, k):
    length = len(food_times)
    answer = 1

    if k>=sum(food_times): return -1

    while k>0: 
        for i in range(length):
            food_times[i] = int(food_times[i])
            if food_times[i]==0:
                answer=answer%length +1
                continue
            else:
                food_times[i]-=1
                k-=1
                answer= answer%length +1
                if sum(food_times)==0:
                    return -1
                elif k==0:
                    return(answer)

#f_times = list(map(int, input().split()))
#a = int(input())

#print(solution(f_times, a))

#뭔가 풀릴거 같은데 안풀려서 오래 붙잡고 있었다.. 다음부터는 쓸데없이 붙잡고 있지 말고 답지, 좋은 코드들 보면서 빨리 익혀야겠다.
# 큐쓰는 문제라던데 자료구조 벌써 까먹은건가,, 다시 공부해야겠다. 
    