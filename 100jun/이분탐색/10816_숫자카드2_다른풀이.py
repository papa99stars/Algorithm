# import sys
# read = sys.stdin.readline

# n = int(read())
# n_num = list(map(int, read().split()))
# m = int(read())
# m_num = list(map(int, read().split()))

# n_num_dic = {}
# for i in n_num:
#     try:
#         n_num_dic[i] += 1 
#     except:
#         n_num_dic[i] = 1

# for i in m_num:
#     try:
#         print(n_num_dic[i] , end = " ")
#     except:
#         print(0, end=" ")


# from bisect import bisect_left, bisect_right
# import sys
# input = sys.stdin.readline
# # card = [6,3,2,10,10,10,-10,-10,7,3]
# # new = [10,9,-5,2,3,4,5,-10]
# M=int(input())
# card = list(map(int, input().split()))
# N=int(input())
# new = list(map(int, input().split()))

# card.sort()

# def binary_code(start, end, target):
#     while start <= end:
#         mid = (start+end)//2
        
#         if target == card[mid]:
#             left = bisect_left(card, target)
#             right = bisect_right(card, target)
#             return right - left
#         elif target > card[mid]:
#             start = mid+1
#         else:
#             end = mid -1
#     return 0

# start=0
# end = M-1
# for i in new:
#     print(binary_code(start, end, i), end= ' ')


# 3
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))
n_num = Counter(n_num)
for i in m_num:
     print(n_num[i], end=" ")

# 4
# import sys
# read = sys.stdin.readline
# _ = read()
# N = map(int,read().split())
# _ = read()
# M = map(int,read().split())
# hashmap = {}
# for i in N:
#     if i in hashmap:
#         hashmap[i] += 1
#     else:
#         hashmap[i] = 1
# print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in M))


