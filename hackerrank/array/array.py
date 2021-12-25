import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result_list = []
    for index in range(n):
        result_list.append(arr[n - index - 1])

    print(*result_list)

## 내장 함수 이용
if __name__ == '__main__':
    n =int(input())

    arr = list(map(int, input().split()))
    arr.reverse()
    for i in arr:
        print(i, end=" ")    