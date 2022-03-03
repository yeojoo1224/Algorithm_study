
def solution(food_times, k):
    length = len(food_times)
    answer = 1

    if k>=sum((food_times[v]) for v in range(length)): return -1

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

    # ft= 
    