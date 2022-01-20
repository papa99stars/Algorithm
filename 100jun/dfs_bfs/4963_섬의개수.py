import sys
sys.setrecursionlimit(10**6)
# dfs를 이용하여 푼 코드 
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
    return False

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 모든 노드(위치)
    result = 0 # 카운트 해주는 변수
    for i in range(n):
        for j in range(m): # (0,1)
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1    
    print(result) # 정답 출력
