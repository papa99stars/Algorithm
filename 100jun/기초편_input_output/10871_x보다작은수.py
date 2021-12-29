n , num = map(int, input().split())
lists = list(map(int, input().split()))
for i in range(len(lists)):
    if lists[i] < num :
        print(lists[i], end = " ")