girl, boy, k = map(int, input().split())
cnt = 0

while girl + boy >= k and girl >= 0 and boy >= 0:
    girl -= 2
    boy -= 1
    cnt += 1

print(cnt - 1)

# while girl >= 2 and boy >= 1 and girl + boy >= k +3:
#   girl -= 2
#   boy -= 1
#   cnt += 1
# print(cnt)
# 조건을 다르게 걸 수도 있음