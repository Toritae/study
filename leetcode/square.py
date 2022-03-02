n = int(input())
k = int(input())

location = [0]
square = []
is_roop_check = True

x,y = 0, 0
dx = {0, 1, 0, -1}
dy = {1, 0, -1, 0}


for i in range(n):
    square.append([])
    for _ in range(n):
        square[i].append(0)
    
    
for _ in range(k*2):
    d = int(input())
    location.append(d)

def dfs(x, y, is_roop_check):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if square[y][x] == 0:
        square[x][y] += 1
    else:
        square[y][x] = 0
    print(square)
    if is_roop_check:
        is_roop_check = False
        dfs(x - 1, y, is_roop_check)
        dfs(x, y - 1, is_roop_check)
        dfs(x + 1, y, is_roop_check)
        dfs(x, y + 1, is_roop_check)
            
    return False
    
for i in range(1, len(location)):
    if i % 2 == 1 :
        x = location[i]
    else:
        y = location[i]
    if x != 0 and y != 0:
        is_roop_check = True
        dfs(x, y, is_roop_check)
        x, y = 0, 0

        
for i in range(n):
    print()
    for j in range(n):
        print(square[i][j],end='')