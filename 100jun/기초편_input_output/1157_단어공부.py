# 문자열 대문자로 변경 string.upper()
# 문자열 소문자로 변경 string.lower()
# 문자가 대문자인지 확인하는 함수 string.isupper()
# 문자가 소문자인지 확인하는 함수 string.islower()
words = input().upper()
unique_words = list(set(words))  
# 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  
    # count 숫자를 리스트에 append
if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])