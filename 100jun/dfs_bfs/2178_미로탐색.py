from collections import deque
n , m = map(int, input().split()) # 주어지는 입력 값 : n , m
graph = [ list(map(int, input())) for _ in range(n) ]
queue = deque() # 확실히 이중으로 받으면 속도가 더 오래 걸림  
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 방향 리스트 
check = [[False]*m for _ in range(n)] 
# check를 통해 방문 O은 True, 방문 x는 False
dist = [[0]*m for _ in range(n)]

# 시작점 
queue.append([0,0])
check[0][0] = True
dist[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m :
            if check[nx][ny] == False and graph[nx][ny] == 1 :
                queue.append([nx,ny])
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True
                
# queue에 있는 시작점 값을 꺼냄
# x,y 증가를 통해 시작점에서 움직임
# 그리고 나서 방문 X & 그리고 graph내에 1로 선정된 곳이면 큐에 추가!! 
# dist는 이동거리를 나타냄
print(dist[n-1][m-1])
