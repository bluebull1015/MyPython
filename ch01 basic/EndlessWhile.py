import random

#answer : 컴퓨터가 기억하고 있는 임의의 값
answer = random.randint(1,100)
print('정답 : %d' % (answer))

count = 0
while True:
    su = int(input('1부터 100 사이의 정수 입력 : '))

    count += 1

    if answer > su:
        print('%s보다 큰 수를 입력해 주세요.' % (su))
    elif answer < su:
        print('%s보다 작은 수를 입력해 주세요.' % (su))
    else:
        print('정답입니다.')
        break
    #end if
#end while
print(count)

