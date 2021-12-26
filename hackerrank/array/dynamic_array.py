#!/bin/python3
import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    # 설정 값: Last_answer를 0으로 
    # array는 2D의 2 by n개의 빈 list로 구성
    # 마지막 출력 값은 하나씩 프린트 해야함 -> 리스트로 
    Last_answer = 0
    arr = [[] for i in range(n)]
    answer = []
    for q in queries:
        if q[0] == 1:
            
            idx  = (q[1]^Last_answer)%n
            arr[idx].append(q[2])
        
        else:
            idx = (q[1]^Last_answer)%n
            temp = q[2]%len(arr[idx])
            Last_answer = arr[idx][temp]
            answer.append(Last_answer)
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()