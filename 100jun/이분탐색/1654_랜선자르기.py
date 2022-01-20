n, m = list(map(int, input().split( )))
array = [ int(input()) for _ in range(n) ]

start = 1
end = max(array)
while(start <= end):
    mid = (start + end) // 2
    lines = 0
    for i in array:
        lines += i // mid
    if lines >= m:
        start = mid + 1
    else:
        end = mid - 1 

print(end)