a, b = map(int, input().split())
result = []
for _ in range(a):
    temp = min(map(int, input().split()))
    result.append(temp)

print(max(result))
