num1 = int(input())
num2 = list(map(int, input()))
result = []
for i in range(len(num2), 0, -1):
  result.append(num1 * num2[i-1])
print(result[0], result[1], result[2], sep='\n')
print(result[0]+(result[1]*10)+result[2]*100)

# 풀이 1
# num1, num2 =map (int,input().split())
# print(num1 * (num2%10))
# print(num1 * ((num2%100)//10))
# print(num1 * (num2//100))
# print(num1 * num2)
# 풀이 2 
# num1 = int(input())
# num2 = input()
# for i in range(len(num2), 0, -1):
#     print(num1 * int(num2[i-1]))
# print(num1 * int(num2))