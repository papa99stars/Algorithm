n = int(input())

d = [0]*91
d[1] = 1
d[2] = 1
for i in range(3,n+1):
  d[i]= 1 + sum(d[0:i-1])

print(d[n])