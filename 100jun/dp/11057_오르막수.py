# 0-9(O) // 10(X),11~9(O) // 22~9(O)

s = [[0] * 10 for i in range(1001)]
# 왜 2중 리스트 일까?
# 첫번째 리스트는 0~9를 나타내고 
# 첫 리스트가 1000개 있으므로 1000줄을 나타냄 
# 즉 s[자릿수][맨끝숫자]
for i in range(10):
    s[1][i] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j + 1):
            s[i][j] += s[i - 1][k]

n = int(input())
print(sum(s[n]) % 10007)