#주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
from itertools import combinations
#import sys
#s = list(map(int, sys.stdin.readline().strip().split())) #숫자들 들어있는 리스트

def solution(nums):
    cnt =0
    result = list(combinations(nums, 3))
    l = len(result) 
    for i in range(l): #조합 리스트의 개수만큼 반복
        summ = sum(result[i]) #각 조합별 합 구하기
        for j in range(2, summ+1): #2부터 합 만큼 돌았을 때
            if summ%j==0: #만약 약수가 존재한다면
                break     #반복문 탈출
        if j==summ: #j가 원래숫자랑 같다면
            cnt +=1 #소수 개수 하나 증가
    return cnt #소수 개수를 반환        

#print(solution(s))
