import sys
sys.setrecursionlimit(10000)

n , m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1) ]
graph[0] = [0,0]
visited = [False for _ in range(n+1)]
count = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def DFS(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        DFS(graph, i, visited)
print(count)