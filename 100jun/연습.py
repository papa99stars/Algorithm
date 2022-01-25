# n, m = map(int, input().split())
# list_1 = []
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
# list_1 = list1 + list2
# list_1.sort()
# for i in list_1:
#     print(i, end= " ")
# import sys
# sys.setrecursionlimit(10**6)

# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m :
#         return False
#     if graph[x][y] == 1 :
#         graph[x][y] = 0
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y+1)
#         dfs(x+1, y-1)
#         dfs(x-1, y+1)
#         dfs(x-1, y-1)
#         return True
#     return False

# while True:    
#     m , n = map(int, input().split())
#     if m == 0 and n == 0 : 
#         break
#     graph = [list(map(int, input().split())) for _ in range(n) ]
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j) == True:
#                 result += 1 
#     print(result)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(x,y):
#         graph[x][y] = 0 
#         for i in range(8):
#             nx, ny = x + dx[i], y + dy[i]  
#             if 0 <= nx < w and 0 <= ny < h and graph[nx][ny]==1 :
#                 dfs(nx, ny)

# while True:
#     h,w = map(int, input().split())
#     if h==0 and w==0:
#         break
#     graph = [list(map(int, input().split())) for _ in range(w)]
#     dx, dy = [-1,1,0,0,-1,-1,1,1], [0,0,-1,1,-1,1,-1,1]
#     cnt=0
#     for i in range(w):
#         for j in range(h):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#                 cnt+=1
#     print(cnt)
