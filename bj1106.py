from sys import maxsize
c, n = map(int,input().split())
ff = []
res = 0
for i in range(n):
    temp = list(map(int,input().split()))
    ff.append(temp)
dp = [0] +[maxsize] * (c+100)
for cost, customer in ff:
        for cur_customer in range(customer, c + 101):
            dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)

print(min(dp[c:c + 101]))