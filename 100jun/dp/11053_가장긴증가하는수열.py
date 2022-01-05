n = int(input())
list_1 = list(map(int, input().split()))
dp = [1]*n
# 여기에서 dp는 n만큼만 해도 가능 
for i in range(n): 
    for j in range(i):  
        if  list_1[i] > list_1[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
# (i = 1 -> j = 0) => list_1[1] > list_1[0] 
# ==> dp[1]은  

# dp리스트에 **자신을 포함해 만들 수 있는 부분** 수열 크기를 저장 
# 현재 위치(i)가 이전에 있는 원소(j)가 큰 지를 확인
# 크다면 dp 값에 1을 더해준다. 
# 단, 현재 위치의 dp[i]가 dp[j]보다 작은 경우에만 적용