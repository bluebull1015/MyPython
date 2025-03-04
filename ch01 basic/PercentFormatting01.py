
name = "김철수" #샵은 주석입니다.
age = 30
height =175.3456789 ; address = '마포'

# % 포맷 코드
print('이름 : %s' % (name))
print('나이 : %d' % (age))
print('키01 : %.3f' % (height))
print('키02 : [%10.4f]' % (height))
print('이름 : %s' % (name))
print('주소 : %s' % (address))

message = '이름은 %s이고, 나이는 %d입니다.'
print(message % (name, age)) #여러 개의 변수 사용시 소괄호 사용

su = 2
bread = '단팥빵'
print('나는 배고파서 %s %d개를 먹었습니다.' % (bread, su))

su01 = 3
su02 = 5
print('%d 더하기 %d는 %d입니다.' % (su01, su02, (su01+su02)))

#f-String을 사용한 문자열 포맷팅
sentense = f"이름 : {name}, 나이 : {age}, 키 : {height:.1f}cm"
print(sentense)

hello = '안녕'
message = '[%10s]' % hello # 오른쪽 정렬 (공백 앞쪽)
print(message)

message = '[%-10s]' % hello # 왼쪽 정렬 (공백 뒤쪽)
print(message)