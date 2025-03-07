#영화 상세정보
import json
import urllib.request
import urllib.parse
from fileinput import filename

import pandas as pd
from fontTools.varLib.models import subList

service_key = '27be3f89d8e2ad852618e56a10658525' # 인증키

# 웹 페이지에서 데이터를 가져 오는 함수
def getDataFromWeb(url):
    request = urllib.request.Request(url)  # 요청 객체
    try:
        response = urllib.request.urlopen(request)  # 응답 객체
        if response.getcode() == 200:  # HTTP 응답 코드 200(OK) 확인
            return response.read().decode('UTF-8')  # 바이트로 변환 후 다시 문자열로 반환
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
    #end try
#end def getDAtaFromWeb(url)

#영화 코드를 입력받아 KOBIS API에서 해당 영화 정보를 JSON 형식으로 가져오는 함수
def movieExtractor(movieCode):
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    parameters = f'?key={service_key}&movieCd={movieCode}'
    url = end_point + parameters
    print(url)

    jsonData = getDataFromWeb(url)

    if jsonData == None:
        return None
    else :
        try:
            return json.loads(jsonData)
        except Exception as err:
            print('JSON 데이터를 읽기를 실패하였습니다.')
            print(err)
            return None
        #end try
    #end if
# end def movieExtractor(movieCode)

# '영화 목록' 서비스에서 크롤링한 엑셀 파일
#pd.read_csv() : 현재 실행 중인 Python 스크립트(또는 Jupyter Notebook)의 "작업 디렉토리(working directory)"에서 파일을 찾는다.
kmdbData = pd.read_csv('kmdb_get_movie_list.csv',encoding='UTF-8')
print(kmdbData.columns) # 데이터프레임의 모든 열(column) 이름을 Index 객체로 반환(kmdbData 데이터프레임에 어떤 열이 있는지 확인하는 코드)
print(len(kmdbData)) #데이터프레임의 전체 행 개수를 반환. 데이터 개수 확인용(kmdbData에 몇 개의 영화 데이터가 있는지 확인하는 코드)
print(kmdbData.head(10)) # head()앞에 있는 거 봄. tail()은 뒤에 있는 거 봄. 디폴트 값은 5개.

movieCodeList = list(item for item in kmdbData['movieCd'])
print(movieCodeList)

cnt = 0 # 카운터 변수
movieCodeLength = len(movieCodeList) # 영화 전체 개수
totalDetailList = list() # 전체 목록을 저장할 리스트


# 영문 필드에 대응하는 한글 이름을 사전으로 작성합니다.
hangulName = {'movieNm': '영화명', 'showTm':'상영시간', 'prdtYear':'제작연도', 'openDt':'개봉연도', 'typeNm':'영화유형'}

# 기존 사전에 다음 요소를 추가하도록 합니다.
#hangulName 사전에 "nationNm"과 "genreNm" 키를 추가하고, 각각 "국가명", "장르명"을 값으로 저장
hangulName['nationNm'] = '국가명'
hangulName['genreNm'] = '장르명'


#주의) "배우이름"과 "감독이름"은 둘 다 'peopleNm'으로 동일한 이름을 사용하고 있습니다.
#차후 if 구문으로 처리할 예정입니다.
hangulName['peopleNm'] = '배우이름'

# 멀티 정보를 담고 있는 요소들의 하위 카테고리 이름 정보를 담는 사전
subtractDict = {'nations':'nationNm','genres':'genreNm', "directors":'peopleNm','actors':'peopleNm'}


print('크롤링 작업 중 입니다. 잠시만 기다려 주세요.')

for movieCode in movieCodeList[0:30]: #편의 상 3개만 추출 후 30개 추출
    cnt += 1
    print(f'{str(cnt)}/{str(movieCodeLength)}번째 작업중 입니다.')
    movieData = movieExtractor(movieCode)
    # print('movieData 결과')
    # print(movieData)

    try:
        onemovie = movieData['movieInfoResult']['movieInfo']
    except Exception as err:
        print(err)
        continue
    #end try

    #목록에 저장하고자 하는 리스트
    concern = ['movieNm', 'showTm', 'prdtYear', 'openDt', 'typeNm']
    for element in concern:
        sublist = list()
        sublist.append(movieCode) # 영화코드
        sublist.append(hangulName[element])
        sublist.append(onemovie[element])
        totalDetailList.append(sublist)
    # end inner for

    maxLimit = 5 #최대 5개까지 추출
    multiple = ['nations', 'genres', 'directors', 'actors']
    for element in multiple:
        # print('^'*30)
        nodeList = onemovie[element]
        print(nodeList)

        idx = 0 # 카운터 변수
        for node in nodeList[0:maxLimit]:
            sublist = list()
            sublist.append(movieCode)

            if element == 'directors':
                hangul_name = hangulName[subtractDict[element]]
            else:
                hangul_name = '배우이름'
            # end if

            idx +=1
            hangul_name = hangul_name + str(idx)

            sublist.append(hangul_name)
            sublist.append(node[subtractDict[element]])
            totalDetailList.append(sublist)
        #end inner for
    #end inner for
# end outer for



movieTable = pd.DataFrame(totalDetailList)
#컬럼명 바꿔주기.
mycolumns = ['movieCode', 'key', 'value']
movieTable.columns = mycolumns # 0,1,2이던 컬럼명을 'movieCode', 'key', 'value'으로 바꿈.

filename =  'kmdb_get_movie_detail_list.csv'
movieTable.to_csv(filename, index=False, encoding='UTF-8')
print(f'{filename}파일이 저장되었습니다.')
print('크롤링이 끝났습니다.')