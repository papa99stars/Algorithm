n = int(input())
list_1 = list(map(int, input().split()))
dp = [1]*n
# 여기에서 dp는 n만큼만 해도 가능 
for i in range(n): 
    for j in range(i):  
        if list_1[j] < list_1[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
# (i = 1 -> j = 0) => list_1[1] > list_1[0] 
# ==> dp[1]은 
# 이렇게 모든 경우를 다 탐색
# 또한 값이 list_1[j] > list_1[i] 나올 경우는 제외 
# 
# dp리스트에 **자신을 포함해 만들 수 있는 부분** 수열 크기를 저장 