n = int(input())
n_num = list(map(int, input().split()))
n_num.sort()
n_num_dic = {}

for i in n_num:
    try:
        n_num_dic[i] += 1
    except:
        n_num_dic[i] = 1 

m = int(input())
m_num = list(map(int, input().split()))

for i in m_num:
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if n_num[mid] == i :
            break
        if n_num[mid] > i :
            end = mid - 1
        else:
            start = mid + 1 
    if n_num[mid] == i :
        print(n_num_dic[i], end = " ")
    else:
        print(0, end = " ")


