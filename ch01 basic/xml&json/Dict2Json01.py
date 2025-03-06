humanDict = {
    'age':20, 'name':'유현석', 'hobby':'독서',
    'address':{'city':'seoul', 'gu':'마포구', 'zipcode':'12345'}
}
print(type(humanDict))
print(humanDict)

import json
#dumps()은 문자열로 변환됨. ensure_ascii=False로 아스키코드에서 한글로 바꿔줌.
#indent는 들여쓰기. sort_keys은 정렬 시켜줌.
humanString = json.dumps(humanDict, ensure_ascii=False, indent=4, sort_keys=True)
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)
print(f'이름 : {humanJson["name"]}')
print(f'취미 : {humanJson["hobby"]}')
print(f'나이 : {humanJson["age"]}')
print(f'시도 : {humanJson["address"]["city"]}')
print(f'군구 : {humanJson["address"]["gu"]}')
print(f'우편 번호 : {humanJson["address"]["zipcode"]}')