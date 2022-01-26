meeting_num = int(input())
clock = []
for i in range(meeting_num):
    clock.append(list(map(int, input().split())))
 
clock.sort()

last, cnt = 0 , 0 
for i, j in clock :
    if i >= last:
        cnt += 1 
        last = j

print(cnt)