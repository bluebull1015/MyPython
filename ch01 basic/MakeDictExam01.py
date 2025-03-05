coffees = {} # empty dict
coffees = dict()

print('자료형 타입', end='')
print(type(coffees))

coffees['에스프레소'] = 1000
coffees['에스프레소'] = 1500
coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마키야또'] = 4000

findItem = '카페라떼' #찾고자 하는 품목

bool = findItem in coffees

if bool:
    print(f'"{findItem}" 항목이 있습니다.')
else:
    print(f'"{findItem}" 항목이 없습니다.')

# '핫초코'가 있는지 확인하고, 없을 경우 5000원으로 추가해 보세요.
findItem = '핫초코'
bool = findItem in coffees

if not bool:
    coffees[findItem] = 5000

print(coffees)


#6000원짜리 품목이 존재하지 않으면, '아이스 커피'를 등록해 보세요.
price = 6000
findItem = '아이스 커피'
bool = price in coffees.values()

if bool:
    print(f'가격이 "{price}"인 항목이 존재합니다.')
else:
    coffees[findItem] = price
# end if


# 다음 항목들을 각각 7,000 ~10,000원으로 coffees 사전에 추가해보세요.
listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']

for key in range(len(listCoffee)):
    coffees[listCoffee[key]] = (key+7)*1000 #값 변경

findItem = '핫초코'
print('%s의 가격은 %d원입니다.' % (findItem, coffees[findItem])) #값 가져오기

# 다음 항목들이 존재하면 출력, 그렇지 않으면 5000으로 상품 등록하기.
targetList = ['라벤더', '우유 커피']

for key in targetList:
    try:
        price = coffees[key] #값 읽어오기
        message = '품명 : %s, 가격 : %d'% (key, price)
        print(message)
    except KeyError: #Exception으로도 처리 가능.
        print(f'{key} 키가 존재하지 않아서 신규 추가하도록 합니다.')
        coffees[key] = 5000 #값 변경
#end for

findItem = '둥글레차'
price = coffees.get(findItem, 3000) #get() 함수는 값 읽어오기 및 기본값 지정이 가능
message = '품명 : %s, 가격 : %d' % (findItem, price)
print(message)

findItem = '아이스 커피'
popItem = coffees.pop(findItem)
print(f'목록에서 제거된 {findItem}의 이전 가격은 {popItem}이었습니다.')

del coffees['에스프레소']

print('모든 품목들의 단가 정보 출력')
for (itemKey, itemValue) in coffees.items() : #요소의 첫 번째 자리에 키(Key), 두 번째 자리에 값(Value)
    message = f'항목 {itemKey}의 단가는 {itemValue}원입니다.'
    print(message)

print(coffees)

# keys() 함수와 [] 기호를 사용하여 전체 목록을 출력하시오.
# 단, 다음 품목별은 단가를 변경하여 출력하도록 합니다.
# 500원 인상 : '카페라떼', '카푸치노'
# 500원 인하 : '핫초코'

for key in coffees.keys():

    if key =='카페라떼' or key=='카푸치노':
        coffees[key] +=500
    elif key == '핫초코':
        coffees[key] -=500
    else:
        pass
    #end if
    message = f'{key}의 가격은 {coffees.get(key)}원입니다.'
    print(message)
#end for

coffees.clear()

print(coffees)