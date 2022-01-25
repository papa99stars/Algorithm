# 입력
import sys
read = sys.stdin.readline
n = int(read())
paper = [ list(map(int, read().split())) for _ in range(n) ]

result_min, result_zero, result_plus = 0 , 0 , 0

def cut(x,y,n):
    global result_min, result_zero , result_plus 
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]: # 9등분하기 
                for a in range(3):
                    for b in range(3):
                        cut( x + n//3*a, y + n//3*b, n//3 )
                return
    if check == -1 :
        result_min += 1
    elif check == 0 :
        result_zero += 1
    elif check == 1 :
        result_plus += 1 

cut(0,0,n)
print(result_min)
print(result_zero)
print(result_plus)   

# import sys
# read = sys.stdin.readline

# n = int(read())
# minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

# papers = []
# for _ in range(n):
#     row = list(map(int, read().split()))
#     papers.append(row)


# def check(row, col, n):
#     global minus_cnt, zero_cnt, plus_cnt
#     curr = papers[row][col] 

#     for i in range(row, row + n):
#         for j in range(col, col + n):
#             if papers[i][j] != curr:
#                 next_n = n // 3
#                 check(row, col, next_n)  # 1
#                 check(row, col + next_n, next_n)  # 2
#                 check(row, col + (2 * next_n), next_n)  # 3
#                 check(row + next_n, col, next_n)  # 4
#                 check(row + next_n, col + next_n, next_n)  # 5
#                 check(row + next_n, col + (2 * next_n), next_n)  # 6
#                 check(row + (2 * next_n), col, next_n)  # 7
#                 check(row + (2 * next_n), col + next_n, next_n)  # 8
#                 check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
#                 return

#     if curr == -1:
#         minus_cnt += 1
#     elif curr == 0:
#         zero_cnt += 1
#     elif curr == 1:
#         plus_cnt += 1
#     return


# check(0, 0, n)

# print(minus_cnt)
# print(zero_cnt)
# print(plus_cnt)


# import sys 
# N = int(sys.stdin.readline()) 
# matrix = [] 
# result = [0, 0, 0] 
# for _ in range(N): 
#     matrix.append(list(map(int, sys.stdin.readline().split()))) 

# def count(start_x, start_y, n): 
#     temp = matrix[start_x][start_y] 
#     rtn = [0, 0, 0] 
#     for i in range(n): 
#         for j in range(n): 
#             if temp != matrix[start_x + i][start_y + j]: 
#                 rtn = divide(start_x, start_y, n) 
#                 return rtn 
#     rtn[temp + 1] += 1 
#     return rtn 

# def divide(start_x, start_y, n): 
#     result = [0, 0, 0] 
#     temp = [] 
#     for i in range(3): 
#         for j in range(3): 
#             temp = count(start_x + i* n//3, start_y + j* n//3, n//3) 
#             result[0] += temp[0]
#             result[1] += temp[1] 
#             result[2] += temp[2] 
#     return result 

# result = count(0, 0, N)
# print(result[0]) 
# print(result[1]) 
# print(result[2])