n = int(input())
for i in range(n):
  string  = list(input().split())
  for j in string:
    print(j[::-1], end=" ")

##
# import sys
# N = int(input())

# for _ in range(N):
#     str = sys.stdin.readline().rstrip()
#     words = list(str.split())
#     reverse_words = []
#     for word in words:
#         reverse_words.append(word[::-1])
#     answer = " ".join(reverse_words)
#     print(answer)