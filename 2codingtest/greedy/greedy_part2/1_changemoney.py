n = 1260
count = 0

type = [500, 100, 50, 10]

for coin in type:
    count += n // coin
    n %= coin

print(count)
