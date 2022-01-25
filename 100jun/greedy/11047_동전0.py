n , m = map(int, input().split())
type = []
for _ in range(n):
    type.append(int(input()))

type.sort(reverse=True)
count = 0

for coin in type:
    count += m // coin # 몫값
    m %= coin

print(count)