t = int(input())
for _ in range(t):
    score_ox = list(input())
    sum = 0 
    c = 1 
    for i in score_ox:
        if i == "O":
            sum += c
            c += 1
        else:
            c = 1 
    print(sum)


# 연속된 문자 처리 방법
