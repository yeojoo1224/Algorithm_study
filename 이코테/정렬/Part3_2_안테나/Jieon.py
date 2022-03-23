n=int(input())
house=sorted(list(map(int,input().split())))

print(house[(n-1)//2])

# 답지봄, 바보인가?
# 왜 중간값을 생각 못하고 평균값을 생각한거지? 중학생 수학 수준인데 현타왔다.
