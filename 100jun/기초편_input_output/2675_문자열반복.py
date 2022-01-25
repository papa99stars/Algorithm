T = int(input())
for _ in range(T):
    num , word = input().split()
    num = int(num)
    word_1 = list(str(word))
    for w in word_1:
        print(w*num, end='')
    print()