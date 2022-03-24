import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

print(min(s), max(s))