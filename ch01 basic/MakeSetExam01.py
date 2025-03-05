coffees = set()

print('자료형 타입 : ', end='')
print(type(coffees))

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노')

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

newItems = ['콜드브루', '고구마라떼', '디카페인커피']
coffees.update(newItems)

# 집합은 순서가 없으므로, 인덱싱/슬라이싱 불가능
# print(coffees[3]) # TypeError: 'set' object is not subscriptable 발생.

findItem = '카푸치노'
bool = findItem in coffees
print(f'{findItem} 존재여부 : {bool}')

# '마키야또'가 존재하는 지 확인하고, 없으면 추가해 보세요.
findItem = '마키야또'
if not findItem in coffees :
    coffees.add(findItem)
# end if

# '마키야도'가 삭제
findItem = '믹스커피'
coffees.remove(findItem)

# '바닐라라떼'를 삭제하되, 항목이 없으면 예외처리 하세요.

try:
    findItem = '바닐라라떼'
    coffees.remove(findItem)
except KeyError:
    print(f'\'바닐라라떼\' 메뉴는 존재하지 않습니다.')
#end try

print('반복문을 이용한 출력')
for element in coffees:
    print(element)

print(f'요소 개수 : {len(coffees)}')

print(coffees)

print('집합 연산')
store01 = set(['고구마라떼', '에스프레소', '아메리카노', '마키야또'])
store02 = set(['아메리카노', '마키야또', '카페라떼', '디카페인커피'])

print('두 매장에서 판매 가능한 품목')
# |기호도 가능합니다.
# union_set = store01 | store02
union_set = store01.union(store02)
print('합집합 : %s' % union_set)

print('두 매장에서 공통적으로 판매 가능한 품목')
# &기호도 가능합니다. 매장별 판매하는 가전제품들을 분석할 때 사용 가능
# intersection_set = store01&store02
intersection_set = store01.intersection(store02)
print('교집합 : %s' % intersection_set)

print('1번째 매장에서만 판매 가능한 품목')
# -기호도 가능합니다.
# difference_set01 = store01-store02
difference_set01 = store01.difference(store02)
print('차집합(A-B) : %s' % difference_set01)

print('2번째 매장에서만 판매 가능한 품목')
# -기호도 가능합니다.
# difference_set02 = store02-store01
difference_set02 = store02.difference(store01)
print('차집합(B-A) : %s' % difference_set02)

symmetric_difference_set = store01.symmetric_difference(store02)
print('차집합들의 합집합 : %s' % (symmetric_difference_set))






