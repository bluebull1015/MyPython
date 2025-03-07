import re


print('문자열 2개와 숫자 3개로 구성된 항목들 찾기')
mylist= ['ab123', 'cd456', 'ef789', 'abc12']

# regex = '[a-z]{2}[0-9]{3}' #정규 표현식
regex = '[a-z]{2}\d{3}' #정규 표현식
pattern = re.compile(regex) #정규식 패턴. compile(): 정규 표현식(Regular Expression, regex)을 미리 컴파일하여 패턴 객체로 변환하는 함수

for item in mylist:
    if pattern.match(item): #정규 표현식 패턴과 문자열을 매칭하는 코드
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    #end if
#end for
print()
print('문자열 "a"와 ".txt" 사이에 숫자가 최소 3개 이상인 항목들')
mylist02 =['a1.txt', 'a12.txt', 'a123.txt', 'a1234.txt']
regex = 'a[0-9]{3,}.txt'
pattern = re.compile(regex)

for item in mylist02:
    if pattern.match(item): #정규 표현식 패턴과 문자열을 매칭하는 코드
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    #end if
#end for
print()
print('문자열 "c"와 "t" 사이에 "a"가 1번 이상인 항목들')
mylist03 =['at', 'cat', 'caat', 'caaat']
# regex = 'ca{1,}t'
regex = 'ca+t'
pattern = re.compile(regex)

for item in mylist03:
    if pattern.match(item): #정규 표현식 패턴과 문자열을 매칭하는 코드
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    #end if
#end for