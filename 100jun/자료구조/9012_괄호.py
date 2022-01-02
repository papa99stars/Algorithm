T = int(input())
for i in range(T):
    vps = list(input())
    sum = 0
    for i in s:    
        if i == "(" :
            sum += 1
        elif i == ")":
            sum -= 1 
        if sum < 0:
            print("NO")
            break
    if sum > 0 :
        print("NO")
    elif sum == 0:
        print("YES")

# stack 구조 형식으로
# num = int(input())
# for i in range(num):
#   input_data = input()
#   bracket = []
#   for j in input_data:
#     if j == "(":
#       bracket.append(j)
#     elif j == ")":
#       if len(bracket) != 0 and bracket[-1] == "(":
#         bracket.pop()
#       else:
#         bracket.append(")")
#         break
#   if len(bracket) == 0:
#     print("YES")
#   else:
#     print("NO")