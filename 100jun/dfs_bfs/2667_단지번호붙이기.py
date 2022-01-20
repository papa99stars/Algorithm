import sys
sys.setrecursionlimit(10**6)
# dfs를 이용하여 푼 코드 

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        global count 
        count += 1 # 일단 global로 정의하면 이 친구는 어디서든 호출이 가능 
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True        
    return False

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
count = 0 # 먼저 변수 정의 
result = 0
num = [] 
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            num.append(count)
            result += 1  
            count = 0  # 다시 초기화 

num.sort()
print(result) # 정답 출력
for i in range(len(num)):
    print(num[i])

# global을 이용해 풀려 했으나 안됌!! 7