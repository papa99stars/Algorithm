import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
def dfs(x): #DFS 함수 정의
    visited[x] = True #방문 체크
    number = numbers[x] #다음 방문 장소
    if not visited[number]: #방문하지 않았다면
        dfs(number) #재귀

for _ in range(int(input())): # 테스트 케이스
    N = int(input()) # 리스트의 총 수     
    numbers = [0] + list(map(int, input().split())) # 1부터 시작하기 위해서
    visited = [True] + [False] * N #방문여부확인용
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]: #방문하지 않았다면
            dfs(i) #DFS실행
            result += 1 #결과값 += 1
    print(result)



# import sys
# sys.setrecursionlimit(100000)
# # Recursion limit을 늘려줘서 에러를 방지

# T = int(input()) # T개의 테스트
# for _ in range(T):
#     N = int(input()) # 순열을 받음 
#     permutation = list(map(int, input().split(" ")))
#     graph = {n + 1 : [permutation[n]] for n in range(N)} # 순열을 그래프로
#     # {1: [3], 2: [2], 3: [1], 4: [5], 5: [4]} 이 형태로 출력 

#     # dfs로 탐색하여 진행경로(trace)상에 있는 노드중에 한번 방문한 노드가 있다면
#     # 순환구조로 판별하고 return한다. 진행경로는 갈림길마다 하나씩 reset 하므로
#     # 해당 노드의 모든 갈래길을 다 탐색한 후에는 해당 노드를 지워주어야 한다.
#     # 또 한번 탐색된 노드는 다시 방문했을때 순환구조가 중복 count 될 수 있으므로
#     # 진행경로 추적을 위한 set 말고 방문 기록을 남기기 위한 set을
#     # 추가적으로 만들어서 기록한다. 그리고 trace를 통해 순환 구조가 발견되면
#     # count를 하나 증가시키면서 탐색을 마치고 visited에 의해 탐색이 마쳐질 경우는
#     # count를 올리지 않아야 한다.

#     visited = set()
#     cicle_count = [0]
#     def dfs(v, trace = set()):
#         if v in trace:
#             cicle_count[0] += 1
#             return
#         if v in visited:
#             return
#         visited.add(v)
#         trace.add(v)
#         for w in graph[v]:
#             dfs(w, trace)
#         trace.remove(v)
#     for v in list(graph):
#         dfs(v)
#     print(cicle_count[0])