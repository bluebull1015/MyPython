print('이름 입력 : ', end='') #end = '' 옵션은 엔터키를 누르지 않겠다.
name = input()

print('나이 입력 : ', end='')
age = input() #input함수는 문자열로 인식한다.
age = int(age) #파이썬에서의 정수형 형변환

print('키 입력 : ', end='')
height = float(input()) #실수 타입 변환. 한줄로도 가능

print('이름 : %s' % (name))
print('나이 : %d' % (age))
print('나이 : %.2f' % (height)) #포맷팅시, 표시된 자릿수까지 유지하고 다음 자리 숫자를 기준으로 반올림


#f-String을 사용한 문자열 포맷팅
sentense = f"이름 : {name}, 나이 : {age}, 키 : {height:.1f}cm"
print(sentense)