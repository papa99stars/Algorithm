num, k = map(int, input().split())
list_1 = [i for i in range(1,num+1)] 
result = []
circle_step = k -1

for i in range(num):
  if len(list_1) > circle_step:
    result.append(list_1.pop(circle_step))
    circle_step += k - 1
  elif len(list_1) <= circle_step:
    circle_step = circle_step % len(list_1)
    result.append(list_1.pop(circle_step))
    circle_step += k - 1   

print("<", ', '.join(str(i) for i in result), ">", sep = '')