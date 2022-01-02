import sys 
n = int(sys.stdin.readline())
list_1 = []
for i in range(n):
    list_1.append(list(map(int, sys.stdin.readline().split())))
list_1.sort(key = lambda x: (x[1], x[0]))
for i in list_1:
    print(i[0], i[1])