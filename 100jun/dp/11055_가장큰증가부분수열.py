n = int(input())
list_1 = list(map(int, input().split()))

dp = [i for i in list_1]

print(dp)
# for i in range(n):
#     for j in range(i):
#         if list_1[i] > list_1[j]:
#             dp[i] = max(dp[i], dp[j] + lst[i])
# print(max(dp))
