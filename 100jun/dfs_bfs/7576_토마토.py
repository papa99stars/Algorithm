# 그 전까지의 문제는 입력된 행렬을 한번만 파악하면 됬으나 
# 이 문제의 경우에는 append하면서 계속 추가 시켜야함 
# 다시 생각해보니, 길 찾기와 같은 문제라고 생각됨 
# dfs로 삽질 함 ㅎㅎㅎ 다시 가즈아 

# 문제에서 "최소일수", "주변의 토마토들을 익힘" 
# => bfs를 사용해 문제 해결 * dfs를 사용 x

from collections import deque
# deque 모듈 안쓰면 시간복잡도 박살남
# (pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)

m, n = map(int, input().split()) # n은 행 수 m은 열 수 
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([]) # 좌표를 받으므로 [ ] 형태로 넣기
# []이거 안 넣어도 문제는 맞음  차이가 뭘까??
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 방향 리스트 
res = 0 # 정답이 담길 변수 

# queue에 처음에  받은 토마토의 위치 좌표를 append
for i in range(n): # n은 행
    for j in range(m): # m은 열 
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1 
                queue.append([nx, ny]) # queue에 계속해서 추가가 됨 

bfs()
for i in graph:
    for j in i:
        if j == 0 :
            # print(graph)
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
# print(queue)
# print(graph)
# 토마토가 모두 익은 상태면 0을 출력, 모두 익지 못하면 -1을 출력 
# 모두 익을 때까지의 최소의 날짜를 출력 