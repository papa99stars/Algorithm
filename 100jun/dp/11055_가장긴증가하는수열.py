n = int(input())
list_1 = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if list_1[j] < list_1[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))