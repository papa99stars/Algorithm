n = int(input())
list_1 = list(map(int, input().split()))

dp = [i for i in list_1]

for i in range(n):
    for j in range(i):
        if list_1[i] > list_1[j]:
            dp[i] = max(dp[i], dp[j] + list_1[i])
print(max(dp))

# 11053과 차이점은 2개가 있다
# 1. dp를 받는 방식  


# n=int(input())
# array=list(map(int, input().split()))

# d=[1]*n
# d[0]=array[0]
# for i in range(1,n):
#   for j in range(i):
#     if array[j]<array[i]:
#       d[i]=max(d[i], d[j]+array[i])
#     else:
#       d[i]=max(d[i], array[i])

# print(max(d))