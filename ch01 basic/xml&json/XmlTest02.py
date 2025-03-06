from xml.etree.ElementTree import Element, SubElement, ElementTree

mydict = {'hong' : ('홍길동',60, 70, 80), 'park' : ('박영희', 50, 70, 95)}
print(mydict)

xmlData = Element('students')

#key에는 key값이 대입, mytuple에는 value값이 대입
for key, mytuple in mydict.items():
    saram = SubElement(xmlData, 'student')
    saram.attrib['id'] = key #속성을 'id'로 하고 속성에 key로 값을 줌.

    #XML은 문자로 넣어줘야하기에 str로 형변환해야 함.
    kor = mytuple[1]
    eng = mytuple[2]
    math = mytuple[3]

    total = kor+ eng + math
    average = total/3.0

    saram.attrib['총점'] = str(total)
    saram.attrib['평균'] = '%.3f' % average

    #saram에 '이름'이라는 태그로 태그를 만들고 mytuple의 데이터 값을 넣어줌.
    SubElement(saram, '이름').text = mytuple[0]
    SubElement(saram, '국어').text = str(kor)
    SubElement(saram, '영어').text = str(eng)
    SubElement(saram, '수학').text = str(math)

#end for

def indent(elem, level=0):
    """
    XML 요소에 들여쓰기를 적용하는 함수.

    Args:
        elem: XML 요소 (ElementTree.Element 객체)
        level: 현재 들여쓰기 수준 (기본값: 0)

    Returns:
        None (입력된 XML 요소가 직접 수정됨)
    """
    mytab = '\t'  # 탭 문자 사용
    i = '\n' + level * mytab  # 현재 수준(level)에 맞는 개행 및 들여쓰기 문자열 생성

    if len(elem):  # 요소에 하위 요소가 있는 경우
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab  # 요소의 텍스트가 없거나 공백뿐이면 적절한 들여쓰기 적용

        if not elem.tail or not elem.tail.strip():
            elem.tail = i  # 요소의 뒤쪽(tail) 공백 정리

        for elem in elem:  # 하위 요소에 대해 재귀적으로 indent 적용
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i  # 마지막 요소의 tail도 정리
    else:  # 하위 요소가 없는 경우 (self-closing 태그)
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i  # 부모 요소와 동일한 수준의 tail 적용
# end def

indent(xmlData) # xml을 보기 좋게 적절한 들여 쓰기와 엔터키 누름.

xmlFile = 'XmlTest_02.xml'
ElementTree(xmlData).write(xmlFile, encoding='UTF-8')
print(xmlFile+'파일이 생성되었습니다.')