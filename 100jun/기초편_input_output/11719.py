# 11719 
# 1
while 1:
  try:
    print(input())
  except EOFError:
    break

# 2 
# 파이썬 라이브러리로 파이썬 인터프리터가 제공하는 변수와 함수를 직접제어할 수 있게하는 모듈
# 여러줄을 입력 받고 싶으면 sys.stdin을 사용(^Z를 입력받으면 종료)
import sys
for line in sys.stdin:
  print(line, end = '')

# input() 으로도 문자열을 입력받을 수 있지만 여러줄을 받아야할 때
# input 을 사용한다면 시간초과가 발생할 수 있다.
# 이럴 때  (입력값이 많거나 크면 ) 주로 sys.stdin.readline() 을 사용한다.
# 이때 \n 를 포함한다는 것도 기억! 