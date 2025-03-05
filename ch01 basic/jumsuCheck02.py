from os.path import split

from numpy.ma.extras import average

myencoding = 'UTF-8'

source = open(file='jumsu.txt', mode='rt', encoding=myencoding) # 읽어 올 파일

destination = open(file='result.txt', mode='wt', encoding=myencoding)#신규 생성할 파일

students = [item.strip() for item in source.readlines()]
print(students)

for bean in students:
    human = bean.split(',')
    # print(human)

    name = human[0]
    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])
    _gender = human[4].upper() #cf : lower() 함수

    total = kor+eng+math
    average = total/3.0
    if _gender == 'M': #or _gender =='m':
        gender = '남자'
    else:
        gender = '여자'
    #end if
    # '이름/성별/총점/평균' 형식
    sentences = '%s/%s/%.1f/%.2f\n' % (name, gender, total, average)
    print(sentences)
    destination.write(sentences)
#end for

source.close()
destination.close()
print('finished')