import sys
sys.setrecursionlimit(2000)
def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    
    else:    
        dfs(number)

for _ in range(int(input())):
    n = int(input())
    numbers = [0] + list( map( int, input().split() ) )
    visited = [True] + [False]*n
    # s = []
    # s.append([i for i in range(1, n+1)])
    # s.append(list(map(int, input().split())))
    result = []

    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
        
    print( n - len(result) )

# 10451과 유사함 
# 다른 점은 반드시 team의 마지막 학생은 첫 학생을 지목해야한다. 