filename = 'jumsu.json'

myfile = open(file=filename, mode='rt', encoding='UTF-8')
mystring = myfile.read() #리스트 안에 사전. 여러 사전을 받기 위해 리스트로 감쌈.
print(type(mystring))
# print(mystring)

import json
jsonData = json.loads(mystring) #리스트 안에 튜플. loads() : JSON 문자열을 파이썬 객체(딕셔너리 또는 리스트)로 변환하는 함수
print(type(jsonData))

#[{'name': '이연수', 'kor': '60.0', 'eng': '70.0', 'math': '80.0', 'hello': '여러분 안녕~~', 'gender': 'F'}, {'name': '강민섭', 'kor': '65.0', 'eng': '75.0', 'math': '85.0', 'gender': 'M'}]
#학생들의 정보를 tuple 형식으로 담고 있는 list
humanList = list()

for human in jsonData:
    name = human['name']
    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor+eng+math

    if 'hello' in human:
        message = human['hello']
    else:
        message = '냉무'
    #end if

    #중간 과정에서만 사용하는 변수 또는 임시 변수에는 _(언더스코어)를 붙여 코드의 가독성을 높일 수 있다.
    _gender = human['gender'].upper()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    #end if
    mytuple = (name, kor, eng, math, total, gender, message)
    humanList.append(mytuple)
#end for
print(humanList)





myfile.close()