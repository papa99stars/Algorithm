#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def hourglassSum(arr):
    maxSum = -63
    width = len(arr[0]) - 2
    length = len(arr[1]) - 2
    for i in range(0,width):
        for j in range(0,length):
        
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])         
            # sum of the mid element
            mid = arr[i+1][j+1]            
            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
        
    return maxSum
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()