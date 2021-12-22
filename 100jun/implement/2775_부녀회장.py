T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())
    people = [ i for i in range(1, num+1)]
    for __ in range(floor):
        for j in range(1,num):
            people[j] += people[j-1]
        # print(people) : 각 층의 거주자 수 출력
    print(people[-1])
