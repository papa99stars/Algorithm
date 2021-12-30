T = int(input())
temp = []
for i in range(T):  
  temp.append(int(input()))
temp.sort()
for i in range(0,len(temp)):
  print(temp[i])

# import sys
# T = int(input())
# temp = [] 
# for i in range(T):
#   temp.append(int(sys.stdin.readline()))
# temp.sort()
# for i in range(T):
#   print(temp[i])