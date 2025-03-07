#영화목록

import pandas as pd
#다운로드 받은 파일의 정보 보기(데이터 구조를 파악하여 분석. 행열 개수, 무슨 타입, 무엇으로 구성 등등)
myencoding = 'UTF-8'
filename = 'kmdb_get_movie_list.csv'
dataframe = pd.read_csv(filename, encoding=myencoding)
print(type(dataframe)) # 타입이 DataFrame이다.

print('\n행 색인 정보 확인')
print(dataframe.index) #index는 행을 가리킨다.

print('\n열 색인 정보 확인')
print(dataframe.columns) #columns는 열을 가리킨다.

for column in dataframe.columns:
    print('-'*50)
    print(column) #컬럼명 출력.
    print(dataframe[column].unique()) # 데이터베이스의 DISTINCT와 비슷하다. unique() : 해당 컬럼에서 중복을 제거한 "고유한 값(unique values)"을 반환

print('\n컬럼별 데이터 유형 확인')
print(dataframe.dtypes) #각 열의 데이터 타입을 나타내는 속성

#변경 전과 변경 후의 데이터를 확인하기 위한 코드(데이터가 너무 많기 때문)
print('\n숫자 형식만 추출')
print('before count : ' + str(len(dataframe)))
# 문자열 컬럼 내부에는 str 키워드가 내재되어 있습니다.
# isdigit()는 숫자 형식의 문자열이면 True가 반환됩니다.
#movieCd 컬럼에서 숫자로만 이루어진 행만 필터링하여 새로운 데이터프레임을 만드는 코드
#Pandas의 "문자열 연산(str accessor)"을 위한 속성
dataframe = dataframe[dataframe['movieCd'].str.isdigit()]
print('after count : ' + str(len(dataframe))) # str(len(dataframe)) : 행(row) 개수

# dataframe.size : 데이터 프레임의 원소 개수
print('\n장르 이름(repGenreNm)이 누락되지 않는 데이터만 추출')
print('before size : ' + str(dataframe.size))

#결측치 : 데이터셋(표(table) 형태의 집합)에서 값이 누락된 상태를 의미하며, None, NaN, null 등으로 표현됨
#notna() : "결측치가 아닌(True) 값만 선택"하는 메서드입니다.
#결측치가 아닌 데이터는 True를 반환합니다.
dataframe = dataframe[dataframe['repGenreNm'].notna()]
print('after size : ' + str(dataframe.size)) # str(dataframe.size) : 전체 원소 개수 (행 × 열)

#전처리(Preprocessing, 분석이나 모델링을 위해 데이터를 정리하고 변환하는 과정) 전 출력.
# print(dataframe.dtypes)
# movieCd 열을 숫자 형식으로 변환(object -> int64). 데이터 전처리 과정 중 "데이터 타입 변환"을 수행하는 작업
dataframe['movieCd'] = pd.to_numeric(dataframe['movieCd'])
#전처리(Preprocessing, 분석이나 모델링을 위해 데이터를 정리하고 변환하는 과정) 후 출력.
# print(dataframe.dtypes)

print('\n제작 년도(prdtYear) 기초 통계량 확인')
prdtYear = dataframe['prdtYear']
print(type(prdtYear))

print('시리즈 요소 개수 확인 : ' + str(prdtYear.size)) #결측치(NaN 포함) 여부와 상관없이 총 요소 개수를 반환
print('prdtYear.shape : ' + str(prdtYear.shape)) #Series의 모양(차원)을 (행 개수, 열) 형태의 튜플로 반환
print('len(prdtYear) : ' + str(len(prdtYear))) #size와 동일하게 결측치 포함한 전체 요소 개수 반환
# count() 함수는 결측치를 제외한 유효한 데이터 갯수
print('prdtYear.count() : ' + str(prdtYear.count())) #NaN(결측치)을 제외한 "유효한 데이터 개수"만 반환(제작 연도가 없는 데이터는 제외하여 출력)

# 이 코드는 데이터 정리(전처리) 전에 "결측치 존재 여부"와 "중복 데이터 여부"를 체크하는 과정
print('누락된 데이터가 있나요?' + str(prdtYear.hasnans)) #결측치(NaN)가 포함되어 있는지 확인 (True/False)
print('모든 항목이 unique한가요?' + str(prdtYear.is_unique)) #모든 값이 중복 없이 고유한지 확인 (True/False)

print('prdtYear.quantile() : ' + str(prdtYear.quantile()))
# 기본적으로 50% 분위수(중앙값) 반환 (q=0.5, median과 동일)
# 분위수를 통해 데이터의 특정 지점을 확인할 수 있음
print('prdtYear.min() : ' + str(prdtYear.min()))# 최솟값 (가장 작은 값 반환)
print('prdtYear.max() : ' + str(prdtYear.max()))# 최댓값 (가장 큰 값 반환)
print('prdtYear.mean() : ' + str(prdtYear.mean()))# 평균 (모든 값을 더한 후 개수로 나눈 값)
print('prdtYear.median() : ' + str(prdtYear.median()))# 중앙값 (데이터를 정렬했을 때 한가운데 있는 값, 50% 분위수)
print('prdtYear.std() : ' + str(prdtYear.std())) # 표준 편차 (데이터가 평균에서 얼마나 떨어져 있는지 측정)
print('prdtYear.sum() : ' + str(prdtYear.sum()))# 총합 (모든 값을 더한 값)


filename = 'kmdb_get_movie_list_preprocessing.csv'
dataframe.to_csv(filename, index=False, encoding='UTF-8')
print(f'{filename}파일이 저장되었습니다.')

