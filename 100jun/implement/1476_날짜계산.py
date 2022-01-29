# a, b, c = map(int, input().split())

# cnt = 1 

# while True:
#     for i in range(1,16):
#         for j in range(1,29):
#             for k in range(1,20):
                 
#                 if a == i and b == j and c == k :
#                     print(cnt)
#                     break
#                 cnt += 1
a, b, c, cnt =1,1,1,1
i_a , i_b , i_c = map(int,input().split())
while(True):
    if i_a==a and i_b==b and i_c==c :
        break
    a+=1
    b+=1 
    c+=1 
    cnt+=1
    if a>=16 : a-=15
    if b>=29 : b-=28
    if c>=20 : c-=19

print(cnt)