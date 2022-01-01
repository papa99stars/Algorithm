#d[i]는 i번째 포도주까지 최대로 마신 포도주의 양이다.(0부터)

# i번째 포도주를 마시고 i-2번째까지 마신 양,
# i,i-1번째를 포도주를 마시고 i-3번째까지 마신 양,
# 그리고 i번째를 마시지 않는 경우(i-1번째 포도주까지 마신 양)를
# 모두 고려해야한다.

n = int(input())
array=[0]*10000
for i in range(n):
  array[i]=int(input())
dp=[0]*10000
dp[0]=array[0]
dp[1]=array[0]+array[1]
dp[2]=max(array[2]+array[0], array[2]+array[1], dp[1])
for i in range(3,n):
  dp[i]=max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3], dp[i-1])
print(max(dp))

# n = int(input())
# w = [0]
# for i in range(n):
#     w.append(int(input()))
# dp = [0]
# dp.append(w[1])
# if n > 1:
#     dp.append(w[1] + w[2])
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
# print(dp[n])