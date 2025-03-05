# def는 define의 줄인 말
# def 함수이름(매개변수01 = [기본값], 매개변수02 = 기본값, ...):
# 매개변수 : argument, parameter, 인자, 인수 등등
def add(first, second=50): # 함수 정의
    return first + second
#and def

su01 = 14
su02 = 5

# positional argument : index 기반 매개 변수 전달 방식
result = add(su01,su02)
print('%d + %d = %d' % (su01,su02,result))
print('%d + %d = %d' % (100, 200, add(100,200)))

# keyword argument : 키워드 기반 매개 변수 전달 방식
su01 = 111
su02 = 222
result = add(second=su01,first=su02)
print('%d + %d = %d' % (su02,su01,result))

#positional argument 방식과 keyword argument 방식이 혼재되어 있음.
result = add(su01, second=su02)
print('%d + %d = %d' % (su02,su01,result))

#기본 값 사용하기. # second=50 #python에는 오버로딩이 없고, 매개변수에 기본값을 넣을 수 있다.
result = add(10)
print('%d' % (result))
