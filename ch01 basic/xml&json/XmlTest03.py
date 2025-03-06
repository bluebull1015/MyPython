import math
from math import sqrt
from xml.etree.ElementTree import parse

# print(math.sqrt(4)) #import 설명을 위해 사용

tree = parse(source='Car_Info.xml') #'Car_Info.xml'가 tree변수에 담김.

myroot = tree.getroot()#root 요소(element)를 가져올 때 사용함.
print(type(myroot))
#<class 'xml.etree.ElementTree.Element'>
# xml.etree.ElementTree: Python의 XML을 다루는 표준 라이브러리.
# ElementTree: XML 트리 구조를 다루는 주요 클래스.
# Element: XML의 개별 요소(노드)를 나타내는 객체.
# <class 'xml.etree.ElementTree.Element'>: XML 요소를 표현하는 객체의 클래스.
carList = myroot.findall('car')
print('총 car 수 : %d' % (len(carList)))
print(type(carList))

#차량 목록 정보를 tuple로 가지고 있는 list
car_list = []

for oneCar in carList:
    print('car 구성 정보')
    # print(oneCar) #car 요소(element)를 순서대로 가져옴.
    brand = oneCar[0].text #car 요소(element)의 0번째 요소(element)를 가져옴.
    brandName = oneCar[0].attrib['name'] #속성(Attribute)을 가져옴.
    model = oneCar[1].text
    year = oneCar[2].text
    color = oneCar[3].text
    print(f'브랜드 : {brand}')
    print(f'브랜드 이름 : {brandName}')
    print(f'모델 : {model}')
    print(f'제작 년도 : {year}')
    print(f'색상 : {color}')

    car_list.append((brand,brandName,model,year,color))

    print('_'*30)
# end for

print(car_list)
#[('현대', 'hyundai', '소나타', '2022', 'White'), ('기아', 'kia', 'k7', '2023', 'Black')]
#[]는 리스트이고 ()는 튜플이다. car_list는 두 개의 원소를 가지고 있고 한 개의 원소당 5개의 변수를 가지고 있다.