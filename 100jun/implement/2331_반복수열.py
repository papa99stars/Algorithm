a, p = map(int, input().split())
num = [a]
while True:
    temp = 0
    for s in  str(nums[-1]):
        temp += int(s)**p
    if temp in nums:
        break
    nums.append(temp)

print(nums.index(temp))