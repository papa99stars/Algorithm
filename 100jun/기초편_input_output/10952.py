# 풀이1 
while 1:
  try:
    a ,b = map(int, input().split())
    if (a ==0) and (b == 0):    
       exit()
    print(a+b)   
  except:
    exit()

# 풀이2
while 1:
    a,b = map(int, input().split())
    if a+b == 0:
        break
    if a == False or b==False:
        break
    print(a+b)