# 6001
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello\nWorld")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print("\"!@#$%^&*()\'")

#6007
print("\"C:\\Download\\'hello'.py\"")

#6008
print('print("Hello\\nWorld")')

#6009
a = input()
print(a)

#6010
a = input()
a = int(a)
print(a)

#6011
a=input()
a = float(a)
print(a)

#6012
a = input()
b = input()
print(a)
print(b)

#6013
a = input()
b = input()
print(b)
print(a)

#6014
a = input()
print(a)
print(a)
print(a)

#6015
a,b = input().split()
print(a)
print(b)

#6016
a,b = input().split()
print(b,a)

#6017
s = input()
print(s,s,s)

#6018
h,m = input().split(':')
print(h,m,sep=':')

#6019
y,m,d = input().split('.')
print(d,m,y,sep='-')

#6020
l,r = input().split('-')
print(l,r,sep='')

#6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022
ymd = input()
print(ymd[0:2])
print(ymd[2:4])
print(ymd[4:6])

#6023
s = input().split(':')
print(s[1])

#6024
a,b = input().split()
s = a+b
print(s)

#6025
a,b = input().split()
r = int(a) + int(b)
print(r)

#6026
a = input()
b = input()
s = float(a)+float(b)
print(s)

#6027
a = input()
b = int(a)
print('%x'%b)

#6028
a = input()
n = int(a)
print('%X'%n)

#6029
a = input()
n = int(a,16)
print('%o'%n)

#6030
n = ord(input())
print(n)

#6031
c = int(input())
print(chr(c))

#6032
c = int(input())
print(-c)

#6033
a = ord(input())
print(chr(a+1))

#6034 - 주의*
a,b = input().split()
c= int(a) - int(b)
print(c) 

#6035
a,b = input().split()
m = float(a)*float(b)
print(m)

#6036
w, l = input().split()
print(w * int(l))

#6037
#반복 횟수와 문장이 줄을 바꿔 입력된다.
n = input()
s = input()
print(int(n)*s)

#6038
#정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a, b = input().split()
c = int(a)**int(b)
print(c)

#6039
a,b = input().split()
c = float(a)**float(b)
print(c)

#6040
a,b = input().split()
print(int(a)//int(b))

#6041
a,b = input().split()
s= int(a)%int(b)
print(s)

#6042
a = float(input())
print(format(a,".2f"))

#6043
f1,f2 = input().split()
s = float(f1)/float(f2)
print(format(s,".3f"))

#6044
a,b = input().split()
x= int(a)
y = int(b)
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)
print(format(float(a)/float(b),".2f"))

#6045
#합과 평균을 공백을 두고 출력한다. 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
a,b,c = map(int, input().split())
sum = a+b+c
avg = format(sum/3, ".2f")
print(sum, avg)

#6046
a = int(input())
print(a<<1)

#6047
a, b = map(int, input().split())
print(a<<b)

#6048
a,b = map(int, input().split())
print(a<b)

#6049
a,b = map(int, input().split())
print(a==b)

#6050
a,b = map(int, input().split())
print(a<=b)

#6051
a,b = map(int, input().split())
print(a!=b)

#6052
a = int(input())
print(bool(a))

#6053
a = bool(int(input()))
print(not a)

#6054
a,b = map(int, input().split())
print(bool(a) and bool(b))

#6055
a,b = map(int, input().split()) #map 함수의 기능: (적용시킬 함수, 함수를 적용할 값) 
print(bool(a) or bool(b))

#6056
a,b = map(int, input().split())
a = bool(a)
b = bool(b)
print((a and (not b)) or ((not a) and b))

#6057
a,b = map(int, input().split())
a = bool(a)
b = bool(b)
print(a==b)

#6058
a,b = input().split()
a = bool(int(a))
b= bool(int(b))
print(not(a or b))

#6059
a = int(input())
print((~a))

#6060
a,b = map(int, input().split())
print(a&b)

#6061
a,b = map(int, input().split())
print(a|b)

#6062
a,b = map(int, input().split())
print(a^b)

#6063
a, b = map(int, input().split())
c = (a if(a>b) else b)
print(c)

#6064
a,b,c = map(int, input().split())
result = ((b if(b<a) else a) if(a<c) else (b if(b<c) else c))
print(result)

#6065
a,b,c = map(int, input().split())
if a%2==0:
 print(a)

if b%2==0:
 print(b)

if c%2==0:
 print(c)

#6066
 a,b,c= map(int, input().split())
if a%2==0:
    print("even")
else:
    print("odd")
    
if b%2==0:
    print("even")
else:
    print("odd")
    
if c%2==0:
    print("even")
else:
    print("odd")

#6067
a = int(input())
if a>0:
    if a%2==0:
        print("C")
    else:
        print("D")
elif a<0:
    if a%2==0:
        print("A")
    else:
        print("B")

#6068
a = int(input())
if a>=90 and a<=100:
    print("A")
elif a>=70 and a<90:
    print("B")
elif a>=40 and a<70:
    print("C")
elif a>=0 and a<40:
    print("D")

#6069
a = input()
if a=='A':
    print("best!!!")
elif a=='B':
    print("good!!")
elif a=='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?")

#6070
a = int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")

#6071
a = int(input())

while a!=0:
    print(a)
    a = int(input())
#6071-ver2
while True:
    a = int(input())
    if a==0:
        break
    else:
        print(a)

#6072
a = int(input())
while a!=0:
    print(a)
    a = a-1
#6072-ver2
a = int(input())
while True:
    if a==0:
        break
    else:
        print(a)
        a = a-1

#6073
a = int(input())

while a!=0:
    print(a-1)
    a = a-1
#6073-ver2
a = int(input())

while a>=1:
    print(a-1)
    a = a-1
#6073-ver3
a = int(input())
while a!=0:
  a = a-1
  print(a)

#6074
n = ord(input())
a = ord('a')
while a<=n:
    print(chr(a))
    a= a+1

#6075
n = int(input())
a = 0
while a<=n:
    print(a)
    a+=1

#6076
a = int(input())

for i in range(a+1):
    print(i)

#6077
a = int(input())
sum =0 

for i in range(2,a+1,2):
    sum = sum+i

print(sum)

#6078
while True:
    n = input()
    if(n=='q'):
        break
    else:
        print(n)
print("q")
#6078_ver2
while True:
    n = input()
    if n=='q':
        print("q")
        break
    else:
        print(n)
#6078_ver3
while True:
    n = input()
    print(n)
    if n=='q':
        break

#6079
n = int(input())
sum =0
i = 1 #i는 1부터-> 왜? 정수를 더하니까

while True:
    if sum<n: #이거 함정이었음- 입력한 수 보다 같거나 작은이 아니라 그냥 작은걸로 해야 결과가 나옴
        sum+=i #i랑 합 변수랑 더해서 다시 합 변수에 저장
        i+=1 #정수 증가
    else:  
        i-=1 #i가 1부터 시작했기 때문에 1빼줌
        break
    
print(i)
#6079_ver2
n = int(input()) #12
sum =0
i = 0

while sum<n: #0 1 3 6 10 
    i+=1     #1 2 3 4 5
    sum+=i   #1 3 6 10 15

print(i)

#6080
n,m= map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)

#6081
#작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
a = input()
n = int(a,16)

for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#6082
n = int(input())

for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end= ' ')

#6083
r,g,b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k, sep=' ')
print(r*g*b)

#6084
h,b,c,s = map(int, input().split())
sum = h*b*c*s/8/1024/1024

print("{:.1f} MB".format(sum))

#6085
w,h,b = map(int, input().split())
sum = w*h*b/8/1024/1024
print("{:.2f} MB".format(sum))
#6085_ver2
w,h,b = map(int, input().split())
#6085_ver3
w,h,b = map(int, input().split())
sum = w*h*b/8/1024/1024
print("%.2f"%sum, "MB")

#6086
n = int(input())
sum = 0
i = 0

while(sum<n):
  i+=1
  sum+=i 
 
print(sum)

#6087
n = int(input())

for i in range (1,n+1):
  if i%3==0:
    continue
  else:
    print(i, end=' ')
    
#6088
a,d,n = map(int, input().split())

print(a+d*(n-1))

#6089
a,r,n = map(int, input().split())

print(a*r**(n-1))

#6090
a,m,d,n = map(int, input().split())

sum = 0

if m==1:
  sum = a+(n-1)*d
else:
  sum = (m**(n-1)*a)+(((m**(n-1)-1)//(m-1))*d)

print(sum)

#6090_ver2
a,m,d,n = map(int, input().split())

for i in range(1,n):
  a = a*m+d

print(a)

#6091
a,b,c = map(int, input().split())
d =1

while d%a!=0 or d%b!=0 or d%c!=0:
  d+=1

print(d)

#6092 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

n = int(input())
s = list(map(int, input().split()))

count =[]

for i in range(24):
  count.append(0)

for i in range(n):
  count[s[i]]+=1

for i in range(23):
  print(count[i+1],end=' ')
#답지는 range(1,24)를 사용했다.

#6093 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
#발상: n의 범위를 꼼꼼하게 파악하지 않았다. -> 다음부터는 for 문에 들어가는 인자와 for문 안에 실행되는 단계 꼼꼼하게 보기!
n = int(input())
s = list(map(int, input().split()))

for i in range(n):
  print(s[n-i-1], end=' ')
  
#6093_ver2
n = int(input())
s = list(map(int, input().split()))

for i in range(n-1, -1, -1):
  print(s[i], end=' ')
  
#6094 출석 부른 번호 중에 가장 빠른 번호 찾기
n = int(input()) #n개의 랜덤번호
k = list(map(int,input().split())) #랜덤번호 k의 집합

k_min = min(k)

print(k_min)

#6095
#오리지날 바둑판 생성
d = []
for i in range(20):
  d.append([]) #리스트 안에 다른 리스트 추가해넣기
  for j in range(20):
    d[i].append(0) #리스트안의 리스트에 0을 추가

n = int(input())
for i in range(n):
  x,y = map(int, input().split())
  d[x][y]= 1


for i in range(1,20):
  for j in range(1,20):
    print(d[i][j], end=' ')
  print()

#6096 십자 뒤집기

#먼저 19 *19 리스트 입력받기

origin = []

for i in range(19):
  origin.append(list(map(int, input().split())))

#십자 뒤집기 횟수 입력
n = int(input())

for k in range(n):
    x,y = map(int, input().split())

    for j in range(19):
        if j==y-1:
            continue
        else:
            if origin[x-1][j]==0:
                origin[x-1][j]=1
            else:
                origin[x-1][j]=0
    
    for i in range(19):
        if i==x-1: continue
        else:
            if origin[i][y-1]==0:
                origin[i][y-1]=1
            else:
                origin[i][y-1]=0

for i in range(19):
    for j in range(19):
        print(origin[i][j], end=' ')
    print()
    
#6097
h,w = map(int,input().split())
n = int(input())

#일단 판 먼저 만들기
pan = [[0] * (w+1) for _ in range(h+1)]

for i in range(n):
  l,d,x,y = map(int, input().split()) #길이, 방향(가로:0, 세로:1), 좌표 xy

  if d==0: #가로 막대면 열이 증가
    dx=x
    dy =y+l-1
  else:
    dx=x+l-1
    dy=y #세로 막대면 행이 증가

  if dx>=1 and dx<=h and dy>=1 and dy<=w: #더한 좌표가 판 범위 이내일 때
    for i in range(x,dx+1):
      for j in range(y,dy+1):
        pan[i][j] =1 #처음범위부터 추가된 범위까지 색칠
        
for i in range(1,h+1):
    for j in range(1,w+1):
        print(pan[i][j], end=' ')
    print()

#6098
miro=[]
for i in range(10):
    miro.append(list(map(int, input().split()))) #miro information input
tmp=1

for i in range(1,10):
    for j in range(tmp,10):
        if miro[i][j]==1:
            tmp = j-1
            break #j break, i comeback
        elif miro[i][j]==2:#break and break
            break
        else:
            miro[i][j]=9        
    if miro[i][j]==2:
        miro[i][j]=9
        break
 
for i in range(10):
    for j in range(10):
        print(miro[i][j],end=' ')
    print()
