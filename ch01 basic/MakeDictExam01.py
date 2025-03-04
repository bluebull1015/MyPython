from keras.src.ops import switch

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
    coffees[listCoffee[key]] = (key+7)*1000

print(coffees)