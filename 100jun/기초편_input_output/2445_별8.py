n = int(input())

plan = n*2
for i in range(1, n+1):
  print("*"*i + " "*(plan - 2*i) + "*"*i)
for i in range(1, n):
  print("*"*(n-i)+ " "*(2*i) +"*"*(n-i))