from tokenize import endpats

mylist01 = [idx for idx in range(1, 5)] #list comprehension이다. 반복문을 사용해서 리스트를 손쉽게 다룸.
print(mylist01)

mylist02 = [10*idx for idx in range(1, 6)]
print(mylist02)

# 1, 4, 7, ..., 100
mylist03 = [idx for idx in range(1, 101, 3)]
print(mylist03)

# 10의 배수들만 필터링
mylist04 = [idx for idx in range(1, 101, 3) if idx % 10 == 0]
print(mylist04)

# 다음 점수 중에서 몇 명이 합격했는지 출력해 보세요.
exam_jumsu = [75, 30, 85, 50] # 합격 기준은 60점 이상
mylist05 = [jumsu for jumsu in exam_jumsu if jumsu>=60]
print(f'총 {len(mylist05)}명 합격')
#예시 총 2명 합격

# 중첩 for
mylist06 = [x*y for x in range(2,10) for y in range(1,10)]
print(mylist06)

# 튜플을 원소로 하는 리스트
fruits = [('바나나', 10), ('사과', 20), ('오렌지', 30)]

#dict comprehension 튜플을 사전으로 바꿈.
mydict01 = {item[0]:item[1] for item in fruits}
print(mydict01)

# 학생들의 시험 점수를 사전으로 만들어 보세요.
students = [
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60)
]

# 튜플 형식의 점수들을 사전의 value로 만드는 예시. dict 컴프리헨션
mydict02 = {one[0]:one[1:] for one in students}
print(mydict02)

#sum 함수는 파이썬 내장 함수 중의 하나
#{'이문식': 220, '강수현': 190, '윤정혁': 170}
mydict02 = {one[0]:sum(one[1:]) for one in students}
print(mydict02)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)