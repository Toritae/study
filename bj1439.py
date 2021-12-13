import sys
a = list(sys.stdin.readline().strip())
s = [a[0]]

for i in range(1, len(a)):
    if a[i-1] != a[i]:
        s.append(a[i])

print(min(s.count('0'), s.count('1')))