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
# s[2][0] += s[1][0]
# s[2][1] += s[1][0~1] 끝 자리수가 1일때, 1보다 작거나 같은 숫자가 올 수 있다.
n = int(input())

print(sum(s[n]) % 10007)