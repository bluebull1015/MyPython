from fileinput import filename

import pandas as pd
pd.set_option('display.max_columns', None)

# 1. CSV 파일 읽기
filename = 'travel.csv'
df = pd.read_csv(filename, encoding='cp949')

# 2. '카테고리' 컬럼이 '여행지'이면서 '펜션'인 데이터만 필터링
filtered_df = df[df['카테고리3'].isin(['여행지','펜션'])]

# 3. 결과를 새 CSV 파일로 저장
filtered_df.to_csv('여행지_필터링.csv', index=False)

print('여행지 데이터 저장 완료!')

# 컬럼 이름에 '여행지'가 포함된 것 모두 출력




