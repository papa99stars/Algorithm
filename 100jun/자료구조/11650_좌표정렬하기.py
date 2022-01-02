import sys 
n = int(sys.stdin.readline())
list_1 = []
for i in range(n):
    list_1.append(list(map(int, sys.stdin.readline().split())))
list_1.sort(key = lambda x: (x[0], x[1]))
for i,j in list_1:
    print(i, j)
# for i in list_1:
#     print(i[0], i[1])

# 시간이 오래 걸림 
# n = int(input())
# list_1 = []
# for i in range(0,n):
#   list_1.append(list(map(int,input().split())))
# list_1.sort(key = lambda x: (x[0], x[1]))
# for i,j in list_1:
#   print(i, j)
