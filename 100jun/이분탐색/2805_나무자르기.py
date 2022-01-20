import sys
read = sys.stdin.readline

n, m = map(int,read().split()) # 나무 수, 필요한 나무 길이
trees = list(map(int, read().split()))
trees.sort()
start, end = 0, max(trees) # 시작 점, 끝점

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    get_tree = 0 # 잘린 나무 합
    for i in trees:
        if i > mid: # mid보다 큰 나무 높이는 잘림
            get_tree += i - mid
            if get_tree > m:
                break

    if get_tree >= m: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)