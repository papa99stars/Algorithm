n = int(input())

d = [0]*91
#d[n]
# n+1로 받으면 일반화된 프로그랭밍 
d[1] = 1
d[2] = 1
for i in range(3,n+1):
  d[i]= 1 + sum(d[0:i-1])
# 역시나 이 문제 또한 규칙을 파악하는 게 중요
# 먼저 자릿수가 늘어나면 
# 자연스레 그 보다 낮은 자릿수는 다 포함 
# 또한 1*0(n-1)의 경우가 생김
print(d[n])



n = int(input())

d = [[0 for _ in range(2)] for _ in range(n+1)]

for r in range(1,n+1):
    if r == 1:
        d[r][0],d[r][1] = 0,1
    else:
        d[r][0] = sum(d[r-1])
        d[r][1] = d[r-1][0]

print(sum(d[n]))