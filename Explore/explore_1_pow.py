# 내장 함수에 대해 알아두기 
# 1009 분산처리 문제를 더 효율적으로 풀 수 있음
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    answer  =  pow(a,b,10)
    if answer == 0:
        answer = 10
    print(answer)            