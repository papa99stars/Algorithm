from collections import deque
import sys
read = sys.stdin.readline

def BFS(v):
    q = deque() # 선입 선출
    q.append(v) 
    visit_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end= " " )
        for i in range(1 , n+1):
            if visit_bfs[i] == 0 and graph[v][i] == 1 :
                q.append(i)
                visit_bfs[i] = 1

def DFS(v):
    visit_dfs[v] = 1
    print(v, end = " ")
    for i in range(1, n+1):
        if visit_dfs[i] == 0 and graph[v][i] == 1 :
            DFS(i) 

n ,m, v = map(int, read().split()) 

graph = [[0] * (n + 1) for _ in range(n+1)]
visit_bfs = [0] *(n + 1) # 
visit_dfs = [0] * (n + 1) # 

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

DFS(v)
print()
BFS(v)