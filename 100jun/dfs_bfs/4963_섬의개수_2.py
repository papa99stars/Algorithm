from collections import deque
import sys
read = sys.stdin.readline
# bfs를 이용한 풀이 
def bfs(x, y):
  dx, dy = [1, -1, 0, 0, 1, -1, 1, -1], [0, 0, -1, 1, -1, 1, 1, -1]
  field[x][y] = 0
  q = deque()
  q.append([x, y])
  while q:
    a, b = q.popleft()
    for i in range(8):
      nx , ny = a + dx[i] , b + dy[i]
      if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
        field[nx][ny] = 0
        q.append([nx, ny])

while True:
  m, n = map(int, read().split())
  if m == 0 and n == 0:
    break
  field = []
  for _ in range(n):
    field.append(list(map(int, read().split())))
  count = 0
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)