#영화목록

import json
import math
import urllib.request
import urllib.parse
import pandas as pd #데이터 분석을 위한 라이브러리이다. 데이터 분석에 쓰인다. pandas 모듈을 pd라는 별칭으로 부르기로 한다(관례적으로).

service_key = '27be3f89d8e2ad852618e56a10658525' # 인증키

# 웹 페이지에서 데이터를 가져 오는 함수
def getDataFromWeb(url):
    request = urllib.request.Request(url) #요청 객체
    try:
        response = urllib.request.urlopen(request) #응답 객체
        if response.getcode() == 200: #HTTP 응답 코드 200(OK) 확인
            return response.read().decode('UTF-8') #바이트로 변환 후 다시 문자열로 반환
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
    #end try
#end def getDAtaFromWeb(url)

# 영화 정보를 추출해주는 함수
def movieExtractor(curPage, itemPerPage):
    end_point = 'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'

    #방법 1 - "URL Encoding 방식" : 딕셔너리를 자동으로 URL 쿼리 문자열로 변환
    # params = {'key':service_key,'curPage':pageNumber,'itemPerPage':pageSize,'openStartDt':thisYear}
    # query_string = urllib.parse.urlencode(params, doseq=True) #doseq은 문자열 변환 및 리스트 데이터를 올바르게 URL 인코딩하는 기능
    # url = f'{end_point}?{query_string}'

    #방법 2 - "f-string 기반 URL 생성 방식"
    parameter = f'?key={service_key}&curPage={curPage}&itemPerPage={itemPerPage}'
    url = end_point +parameter
    print(url)


    jsonData = getDataFromWeb(url)
    if jsonData is None:
        return None
    #end if

    try:
        return json.loads(jsonData)
    except Exception as err :
        print('JSON 데이터에 문제가 있습니다.', err)
        return None
    #end try
#end def movieExtractor

#영화 정보를 저장할 데이터 프레임
movieTable = pd.DataFrame() #DataFrame() : 2차원 데이터(표)를 다루는 객체를 생성하는 함수

# JSON 데이터를 판다스 데이터 프레임으로 반환해주는 함수
def makeMovieTable(movieData):
    global movieTable #이 변수는 전역 변수입니다.
    print('^'*40)
    for onemovie in movieData['peopleListResult']['peopleList']:
        onedict = {
            'peopleCd': onemovie['peopleCd'],
            'peopleNm': onemovie['peopleNm'],
            'peopleNmEn': onemovie['peopleNmEn'],
            'repRoleNm': onemovie['repRoleNm'],
            'filmoNames': onemovie['filmoNames']
        }

        #1개의 영화 정보를 데이터 프레임으로 변환
        oneframe = pd.DataFrame(onedict, index=[0])

        #기존 데이터 프레임에 현재 프레임을 누적
        #pd.concat()의 첫 번째 매개변수(objs)에는 반복 가능한(iterable) 객체가 와야 한다. 즉, 여러 개의 데이터프레임을 담은 리스트나 튜플을 전달해야 한다. 그렇지 않으면 오류가 발생한다.
        movieTable = pd.concat([movieTable, oneframe]) #[]로 묶으면 매개변수 하나로 인식.

    #end for
#end def makeMovieTable(movieData)

print('크롤링 중입니다. 잠시만 기다려 주세요.')

# 기본 설정 값
curPage = 1
itemPerPage = 100 # 1번 시도시 최대 2개까지 추출 가능
wantPage = 10


while True:
    movieData = movieExtractor(curPage, itemPerPage)
    print(movieData)
    print('_'*100)

    if movieData is None:
        break
    # end if

    try:
        totCnt = movieData['peopleListResult']['totCnt']
    except Exception as err:
        curPage += 1
        continue
    #end try

    if curPage == 1:
        print(f'데이터 총 개수 : {totCnt}')

    if totCnt == 0: #데이터가 없으면 종료
        break

    totalPage = math.ceil(totCnt/itemPerPage)
    print(f'진행 중인 페이지 : {curPage}/{totalPage}')

    makeMovieTable(movieData)

    if curPage == wantPage:
        break # 마지막 페이지에 도달했으면 종료
    #end if
    curPage += 1 # 다음 페이지로 이동
#end while



print('크롤링이 끝났습니다..')

# 데이터 확인
print(movieTable)
print(type(movieTable))
print(movieTable.info())

# csv 파일로 저장
# csv : comma separate value 텍스트 파일(메모장으로 볼 수 있음. 엑셀 지원함. 콤마로 구분함.)
filename = 'kmdb13_get_movie_people_list.csv'
movieTable.to_csv(filename, index=False, encoding='UTF-8') #데이터프레임을 CSV 파일로 변환하여 저장.
print(f'{filename} 파일이 저장되었습니다.')
