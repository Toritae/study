# pascal의 삼각형 참고!
import math
T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(bridge)

# def gg(x, y):
#     if x == y or y == 0:
#         return 1
#     return gg(x-1,y-1) + gg(x-1,y)

# nCm