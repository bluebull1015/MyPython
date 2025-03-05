def girlFriendCheck(findName):
    girlFriend = ['은하', '소원', '유주', '예린', '신비', '엄지']

    isMember = findName in girlFriend

    if isMember:
        message = f'{findName}님은 여자 친구 멤버가 맞습니다.'
        print(message)
    else:
        message = f'{findName}님은 여자 친구 멤버가 아닙니다.'
        raise Exception (message)
    #end if
#end def
name = '윤종신'

try:
    girlFriendCheck(name)
except Exception as err: #예외클래스 as 예외객체별칭:
    print(f'예외 발생 : {err}')