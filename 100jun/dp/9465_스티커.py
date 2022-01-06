t = int(input())
for i in range(t):
    s = [] 
    # [ s[0] => 1 2 3
    #   s[1] => a b c ] 
    n = int(input())
    for k in range(2):
        s.append(list(map(int, input().split())))
    for j in range(1,n):
        if j == 1:
            s[0][j] += s[1][j-1]
            s[1][j] += s[0][j-1]
        else:
            s[0][j] += max(s[1][j-2], s[1][j-1])
            s[1][j] += max(s[0][j-2], s[0][j-1])
    print(max(s[0][n-1], s[1][n-1]))

# T = int(input())
# dp = [0]*100000
# for i in range(T):
#     n = int(input())
#     list_1 = list(map(int, input().split()))
#     list_2 = list(map(int, input().split()))
#     dp[0] = max(list_1[0], list_2[0])
#     for i in range(1, n+1):
#         # dp의 식을 더하는 과정인데
#         # -> 1. list_1과 list_2 대각선으로 합을 구한다.
#         # 하지만 여기서 문제가 있다. 마지막 부분에 도달하였을 때,
#         # 리스트의 -1 ~ -3 사이에서는 대각선이 아닌 한번은 쉬고 