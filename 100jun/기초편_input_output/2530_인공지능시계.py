hour, minute, second = map(int, input().split())
take_second = int(input())

second += take_second
minute += second//60
hour += minute//60

second %= 60
minute %= 60
hour %= 24
print(hour, minute, second)
