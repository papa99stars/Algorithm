n = int(input())
for i in range(n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(n - 2, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))

# n = int(input())
# 구현이 다르게 됨 이 코드는 박스째로 코딩이 됌
# for i in range(0, n):
#   print(" "*(i) + "*"*(2*(n-i)-1) + " "*(i))
# for i in range(1, n):
#   print( " "*(n-i-1) + "*"*(2*i+1) + " "*(n-i-1))