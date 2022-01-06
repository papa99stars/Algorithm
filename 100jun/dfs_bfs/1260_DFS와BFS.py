import sys
from collections import deque
# dfs - 재귀
# 스택 구현 시 재귀 함수 이용!  
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
# dfs(n) * dfs(i)

# bfs
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# node, branch, first node
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

# 인접행렬 만들기 
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# sort adjacency list
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
# initialize check list
visited = [False] * (n + 1)
print()
bfs(v)