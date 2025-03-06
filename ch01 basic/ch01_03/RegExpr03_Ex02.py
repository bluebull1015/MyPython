import re
myfile = open(file='myid.txt', mode='rt', encoding='UTF-8')
mylist = [item.strip() for item in myfile.readlines()]
print(mylist)

myfile.close()

for item in mylist:
    regex = '\(\S+\)'
    pattern = re.compile(regex)
    popdata = pattern.search(item)

    # if popdata != None:
    if popdata is not None:
        result = str(popdata.group().replace("(","").replace(")","")) #group() : 정규 표현식에서 매칭된 문자열을 반환하는 메서드
        print(result)
#end for
