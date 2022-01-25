T = int(input())
for _ in range(T):
    list_a = list(map(int, input().split()))
    avg = sum(list_a[1:]) / list_a[0]
    cnt = 0
    for score in list_a[1:]:
        if score > avg:
            cnt += 1 
    rate = (cnt / list_a[0]) * 100
    print(f'{rate:.3f}%')



