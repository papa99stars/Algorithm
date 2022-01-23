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
