#open과 close는 같이 만들어 놓는다.
print('파일에 기록합니다.')
filename = 'mem.txt'
myfile01 = open(file='mem.txt', mode='wt', encoding='UTF-8') # 매개변수 중 file, mode, encoding을 제일 많이 사용함.
print(type(myfile01))

members = ['홍영식', '김민수', '박진철', '강호숙']
for mem in members:
    message = f'\'{mem}\'님 안녕하세요.\n'
    myfile01.write(message)
#end for


myfile01.close()
print(f'{filename} 파일이 생성됨')

print('기존 파일에 내용을 추가합니다.') # at = append text
myfile02 = open(file=filename, mode='at',encoding='UTF-8')

# 홀 수 번째 고객님과 짝수 번째 고객님에 대한 멘트를 다르게 적용해 보기.
for idx in range(len(members)): #숫자를 다뤄야할 때는 range를 사용한다.
    if idx%2==0:
        message = f'{idx}번째 고객 {members[idx]}님 반가워요.\n'
    else:
        message = f'{idx}번째 고객 {members[idx]}님 어서오세요.\n'

    myfile02.write(message)
    #end if
#end for
myfile02.close()

print('반복문을 사용하여 파일을 여러개 만들어 봅니다.')
print('파일 이름 : somefile01.txt ~ somefile10.txt')
for idx in range(1,11):
    # filename = 'somefile' + idx + '.txt' #자바는 가능하나 파이썬은 이 경우암시적 형변환 안됨.
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    # print(filename)
    myfile = open(file=filename, mode='wt',encoding='UTF-8')
    myfile.write(f'나는 "{filename}" 파일입니다. \n')
    myfile.close()
#end for

print('다음 멤버들의 이름을 사용하여 파일을 여러개 만들어 보세요.')
#예시 : '홍영식.txt', '김민수.txt' 등등
members = ['홍영식', '김민수', '박진철', '강호숙']
for idx in range(len(members)):
    filename = f'{members[idx]}' + '.txt'
    myfile = open(file=filename, mode='wt', encoding='UTF-8')
    myfile.write(f'{members[idx]}의 파일')
    myfile.close()
#end for

print('with 구문을 사용하면, close() 함수를 사용하지 않아도 자동으로 closing 동작을 수행합니다.')
with open(file='test.txt', mode='wt', encoding='UTF-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    #file 매개 변수를 변경하여 testfile 파일에 출력하겠습니다. 출력의 방향을 바꾼 것이다.
    #print() 함수의 file 매개변수가 None이거나 생략되면 기본적으로 sys.stdout(즉, 콘솔창)에 출력된다.
    print('hello~world', file=testfile)
# end with

print('finished')