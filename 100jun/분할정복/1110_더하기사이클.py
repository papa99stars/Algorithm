n = num = int(input())
count = 0
while True:
    fir = n // 10
    sec = n % 10
    total = fir + sec
    count += 1
    n = int(str(n % 10) + str(total % 10))
    if(num == n):
        break
print(count)