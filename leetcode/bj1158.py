# Queue 형식

# import sys
# import time
# start = time.time()
# from queue import Queue
# n, k = map(int,sys.stdin.readline().split())
# q = Queue()
# result = []
# for i in range(1, n+1):
#     q.put(i)

# while not q.empty():
#     for i in range(k) :
#         num = q.get()
#         if i == k-1:
#             result.append(num)
#         else:
#             q.put(num)

# print(result)
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# Queue형식의 list

import sys
n, k = map(int,sys.stdin.readline().split())
result = []
people = list(range(1,n+1))
i = k-1
while True:
    result.append(people.pop(i))
    if not people:
        break
    i = (i + k-1) % len(people)
print('<'+', '.join(map(str,result))+ '>')