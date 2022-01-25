# enumerate는 "열거하다"라는 뜻이다. 
# 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다.

# 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.

for i , name in enumerate(['body','foo','bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar
# enumerate를 for문과 함께 사용시 자료형의 현재 순서와 그 값을 쉽게 알 수 있다.
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는
# 인덱스 값이 필요할 때, enumerate 함수를 사용하면 매우 유용하다. 