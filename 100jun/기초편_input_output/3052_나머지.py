count = [] 

for _ in range(10):
    n = int(input()) % 42
    count.append(n)

count = set(count)
print(len(count))