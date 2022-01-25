a = int(input())
b = int(input())
c = int(input())

temp = list(str(a*b*c))

for i in range(10):
    print(temp.count(str(i)))
# temp1 = str(a*b*c) 
# # 통째롤 묶인 채로 들어감 
# temp2 = list(str(a*b*c))
# # 이거는 자릿수마다 하나하나 나누어져 들어감