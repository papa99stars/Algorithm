import sys

n = int(input())
list1 = []
for i in range(n):
    list1.append(input().split())
print(list1)
print(list1.count(0))
print(list1.count(1))
