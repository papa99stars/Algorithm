n, m, k = map(int, input().split())
list_1 = list(map(int, input().split()))

list_1.sort(reverse=True)
first_list_1 = list_1[0]
second_list_1 = list_1[1]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count*(first_list_1)
result += (m-count)*second_list_1

print(result)