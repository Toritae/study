import sys

n = int(sys.stdin.readline())
a = list(map(int,input().split()))
print(min(a) * max(a))