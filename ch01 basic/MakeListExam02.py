#coffees = [] # empty list
import random

coffees = list()
print('자료형 타입 : ', end='')
print(type(coffees))

coffees.append('아메리카노') #끝자락에 넣음
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')
coffees.append('카푸치노')

#tuple과는 다르게 list는 값을 할당할 수 있습니다.
coffees[6] ='막걸리'

#인덱싱
print('앞에서 2번째 음료 : %s' % (coffees[2]))
print('뒤에서 1번째 음료 : %s' % (coffees[-1]))

#슬라이싱 - 순서가 있는 자료구조는 다 인덱스 슬라이싱이 가능하다. set, 리스트, 튜플, 사전, 문자열 등등
print('1번째부터 3번째까지 요소 : %s' % (coffees[1:4]))
print('3번째부터 끝까지 요소 : %s' % (coffees[3:]))
print('처음부터 2번째까지 요소 : %s' % (coffees[:3]))

print('짝수 인덱스 요소만 출력 : %s' % (coffees[0::2]))
print('홀수 인덱스 요소만 출력 : %s' % (coffees[1::2]))
print('색인이 3의 배수인 요소들 출력 : %s' % (coffees[0::3]))

print('오름차순 정렬')
coffees.sort(reverse=True)
print(coffees)

print('내림차순 정렬')
coffees.sort()
print(coffees)

print('무작위로 섞기')
random.shuffle(coffees)
print(coffees)

print('요소 개수 : %d' % len(coffees))


