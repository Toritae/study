def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

n = int(input())
balance =0 # 잔액
m = 0 # 최소금액
b_ = -1 
flag = True
for i in range(n):
    a, b = map(int, input().split())
    m_ = b-a-balance  
    if m_ < 0:
        flag = False
    elif m_ > 0:
        m = gcd(m_,m)
        b_ = max(b_, b)     
    balance = b
    
if flag and m > b_: 
    print(m or 1) # m==0이라면 1을 출력(즉, 충전금액을 사용한 적이 없는 경우)
else: 
    print(-1)
    
# n = int(input())
# n_list = []
# min_add = 9999999999
# money = 0

# for i in range(n):
#     temp = list(map(int,input().split()))
#     n_list.append(temp)

# for i,j in n_list:
#     if i >= 0:
#         money += i
#     elif i < 0:
#         if money >= i:
#             money += i
#         elif money < i:
#             i = i + money
#             print(i-j)
#             min_add = min(min_add, -(i-j))
#             money = j
#     print(min_add)

# print(min_add)
    