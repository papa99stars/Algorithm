a, p = map(int, input().split())
nums = [a]
while True:
    temp = 0
    for s in  str(nums[-1]):
        print(s)
        temp += int(s)**p
        print(temp)
    if temp in nums:
        break
    nums.append(temp)
print("정답:",nums.index(temp))

# 이 문제를 그래프 순회로 푼다는 의미
# 이미 방문한 노드를 재방문하게 되는 순간 순회종료
# 두 배열 visited 배열, 실제 수를 담고 이쓴ㄴ 배열 
# 근접한 노드?? 

# # 문제 상에서 원하는 수열 항 구하기
# def next_num(number):
#     return sum(list(int(elem) ** p for elem in str(number)))
# def dfs(node, visited, cnt):
#     # 이미 방문한 노드인 경우 (여기서 순회 종료!)
#     # 0 : False, 자연수 : True

#     if visited[node]:
#         return visited[node] - 1  # 현재를 재외한 누적 길이

#     # 아직 방문하지 않았다면
#     visited[node] = cnt
#     next_number = next_num(node)
#     cnt += 1
#     return dfs(next_number,visited,cnt)

# a, p = map(int,input().split())
# # flag 변수 역할도 하면서 누적 길이를 구하는 배열
# # 나올 수 있는 가장 큰 수가 9^5+9^5+9^5+9^5=236196 이므로
# # visited의 index는 결국 각각의 항
# visited = [0] * 250000
# # visited 배열 : boolean array(x), 누적 길이
# cnt = 1
# print(dfs(a,visited,cnt))