import json
import urllib.request
import urllib.parse
import math

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
def movieExtractor(pageNumber, pageSize, thisYear):
    end_point = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
    parameter = f'?key={service_key}&curPage={pageNumber}&itemPerPage={pageSize}&openStartDt={thisYear}'
    url = end_point +parameter
    # print(url)

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

# JSON 데이터를 판다스 데이터 프레임으로 반환해주는 함수
def makeMovieTable(movieData):
    pass
#end def makeMovieTable(movieData)

print('크롤링 중입니다. 잠시만 기다려 주세요.')

# 기본 설정 값
startYear, endYear = 2024, 2025
page_size = 100 # 1번 시도시 최대 100개까지 추출 가능
for thisYear in range(startYear, endYear):
    print(f'{thisYear}년도 크롤링 중입니다.')
    pageNumber = 1

    while True:
        movieData = movieExtractor(pageNumber, page_size, thisYear)
        print(movieData)
        print('_'*100)

        if movieData is None:
            break
        # end if

        try:
            totCnt = movieData['movieListResult']['totCnt']
        except Exception as err:
            pageNumber += 1
            continue
        #end try

        if pageNumber == 3:
            print(f'데이터 총 개수 : {totCnt}')

        if totCnt == 0: #데이터가 없으면 종료
            break

        totalPage = math.ceil(totCnt/page_size)
        print(f'진행 중인 페이지 : {pageNumber}/{totalPage}')

        #요기 코딩 예정

        if pageNumber == totalPage:
            break # 마지막 페이지에 도달했으면 종료
        #end if
        pageNumber += 1 # 다음 페이지로 이동
    #end while
#end for


print('크롤링이 끝났습니다..')

# 데이터 확인

# csv 파일로 저장
