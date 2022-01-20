hour , minute = map(int, input().split())
take_time = int(input())

after_min = ( minute + take_time) % 60
after_hour = ( hour + ((minute + take_time) // 60)) % 24

print(after_hour, after_min )

