h, m = map(int, input().split())
if m < 45:
  h -= 1
  m = (60 + m -45)
else:
  m -= 45

if h == -1:
  h = 23

print(h, m)


# time, minute = map(int, input().split(" "))

# new_minute = minute -45

# if new_minute < 0 :
#     time -= 1
#     new_minute += 60
#     if time < 0 :
#         time += 24

# print(time, new_minute)