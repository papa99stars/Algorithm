n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = list1 + list2
ans.sort()
# for i in ans:
#     print(i, end= " ")
print(*ans)
