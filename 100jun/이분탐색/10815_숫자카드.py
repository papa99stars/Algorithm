import sys
read = sys.stdin.readline

n = int(read())
n_num = list(map(int, read().split()))
m = int(read())
m_num = list(map(int, read().split()))
n_num.sort() # 정렬
# 이분탐색할 때 
for i in m_num: 
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if 0 <= mid < n:
            if n_num[mid] < i:
                low = mid + 1
            else: 
                high = mid - 1
        else:
            break
    if 0 <= high + 1 < n:
        if n_num[high + 1] == i: 
            print(1, end=" ")
        else: 
            print(0, end=" ")
    else: 
        print(0, end=" ")

# # 집합이용해서 풀기
# import sys
# read = sys.stdin.readline

# n = int(read())
# n_num = set(map(int, read().split()))
# m = int(read())
# m_num = list(map(int, read().split()))
# for i in m_num:
#     if i in n_num:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
###############################################
# import sys
# from bisect import bisect_right, bisect_left

# n = int(sys.stdin.readline())
# number_cards = list(map(int, sys.stdin.readline().split())) # 가지고 있는 숫자 카드 입력
# number_cards.sort() # 이진탐색을 위한 오름차순 정렬
# m = int(sys.stdin.readline())
# target_numbers = list(map(int, sys.stdin.readline().split())) # 판별해야하는 숫자카드 입력

# # bisect 라이브러리를 활용해 right, left 인덱스 사이에 숫자가 존재하는 지 확인한다.
# for target in target_numbers:
#     left_index = bisect_left(number_cards, target)
#     right_index = bisect_right(number_cards, target)
#     if left_index == right_index:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')