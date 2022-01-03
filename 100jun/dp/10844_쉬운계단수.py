n = int(input())
dp = [[0]*10 for i in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
# 왜 2차원 배열을 사용했을까?
# 
# dp가 담고 있는 것은 무슨 뜻일까?
# 
num_for_div = 1000000000

for i in range(2,n+1):
    for j in range(10):
        # 규칙을 보면 0일때는 1로 결정되고
        # 9일때는 8로 결정 
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9 :
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 그 이외에는 2가지의 경우의 수로 뽑아 나가짐 

print( sum(dp[n]) % num_for_div )
