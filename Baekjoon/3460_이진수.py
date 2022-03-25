import sys
n = int(sys.stdin.readline())

for i in range(n): #2
    binary = []
    num = int(sys.stdin.readline()) #11 9 
    while True:
        binary.append(num%2) #1 1 0 1 
        num = num//2 #11->5, 5->2, 2->1, 1->0 |||  9->4, 4->2, 2->1, 1->0
        if num==0:
            break

    l = len(binary) #이진수 리스트 길이 계산-1 (반복문 고려해서)
    for j in range(l):
        if binary[j] ==1:
            print(j, end=' ')
    print()