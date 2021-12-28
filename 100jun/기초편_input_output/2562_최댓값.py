lists = []
for i in range(9):
    lists.append(int(input()))
# lists = [int(input()) for _ in range(9)]
max_num = max(lists)
max_index = lists.index(max_num) + 1
print(max_num)
print(max_index)