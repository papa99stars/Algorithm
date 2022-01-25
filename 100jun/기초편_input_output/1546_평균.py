n = int(input())
total_score = list(map(int, input().split()))
M = max(total_score)
temp = []
for score in total_score:
    temp.append( (score/M) * 100 ) 
print(sum(temp)/n) 