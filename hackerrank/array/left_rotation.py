import math
import os
import random
import re
import sys

def rotateLeft(d, arr):
    temp = []
    for num in arr[d:]:
        temp.append(num)
    for num in arr[:d]:
        temp.append(num)
    
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

## 좋은 풀이 
# def rotateLeft(d, arr):
#     for _ in range(d):
#         arr.append(arr.pop(0))
#     return arr

# def rotateLeft(d, arr):
#     for i in range(d):
#         j = arr.pop(0)
#         arr.append(j)
#     return arr

# def rotateLeft(d, arr):
#     return arr[d:] + arr[0:d]