import math
def solution(rows, columns, queries):
    answer = []
    table = []
    temp = []
    small = math.inf
    for i in range(rows):
        for j in range(columns):
            temp.append(i*columns+j+1)
        table.append(temp)
        temp =[]
    for query in queries:
        query = [x-1 for x in query] 
        tmp = table[query[0]][query[1]]
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    return answer