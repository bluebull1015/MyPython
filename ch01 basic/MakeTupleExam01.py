
# 목록에 소괄호를 사용하거나, 단순 콤마만 연결하면 tuple이 됩니다.
coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')
coffee03 = '카푸치노', '마키야또'

print('자료형 타입', end='')
print(type(coffee01))

#반복연산자
mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼', '플랫화이트']
coffee04 =tuple(mylist) #list를 tuple으로 변환

#튜플 합치기
# + 기호 사용시 요소 개수가 1개이더라도 반드시 콤마를 붙여 주세요.
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
length = len(coffees)
print('요소 개수 : %d'  %(len(coffees)))
print(coffees)

# 불변성을 가지는 튜플은 값을 할당할 수 없습니다.
#coffees[1] = '우유'

#인덱싱
print('앞에서 3번째 요소 : %s' %(coffees[3]))

print('앞에서 3번째 요소 : %s' %(coffees[-2]))

#슬라이싱
print('1번째부터 3번째까지의 요소 : ', end='')
print(coffees[1:4])

print('4번째 이후의 요소 : ', end='')
print(coffees[4:])

print('3번째 요소까지 출력 : ', end='')
print(coffees[:4])

mycount = coffees.count('아메리카노')
print('아메리카노의 개수 %d' % (mycount))

myindex = coffees.index('아메리카노')
print('아메리카노의 위치 색인 : %d'% myindex)

#튜플의 응용 swep기법
print('튜플의 응용')
x,y = 3,4
print('before x: %d, y:%d'%(x,y))
print('after x: %d, y:%d'%(x,y))