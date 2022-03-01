#거스름돈 문제 모범답안
n = int(input()) #1260
cnt = 0

coin_types = [500,100,50,10]

for i in coin_types:
  cnt += n//i #1260//500, 1260//100 #cnt = 해당 동전 '몇 개'인지 알기
  n = n%i #n = 처음 나눈수의 나머지로 변환

print(cnt)