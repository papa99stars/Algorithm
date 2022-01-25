n = input()
temp = list(str(n))
# print(temp)
temp1 = [] 
for i in temp:
    temp1.append(int(i))
if not 0 in set(temp1):
    print(-1)
elif sum(temp1[:]) % 3 != 0 :
    print(-1)
else:
    temp1.sort(reverse = True)
    for i in temp1:
        print(i, end="")
# 30배수 -> 3배수랑 10배수 
# 10의 배수 : 수 안에 0이 있으면 되고
# 3의 배수  : 각 자릿수를 더한 후에 3으로 나눠떨어지면 ok
