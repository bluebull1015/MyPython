import requests
import urllib.parse
from tqdm import tqdm
import time
import pandas as pd



news_filename = 'da_news_data.csv' #api요청으로 받아온 파일 전체
news_filtered_columns = 'da_news_data_summary.csv' #전체 파일에서 특정 컬럼만 추출
query = '다문화 가정이 겪는 어려움'





def news_api(query, display, start, sort):
    client_id = "mSoJcqj0YQbP29jC1wPl"
    client_secret = "4ITpTS3qUy"
    global response
    url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display={display}&start={start}&sort={sort}"

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error 내용: {response.text}")
    # end if
    # JSON 변환 (딕셔너리 형태로 변환됨)
    return response.json()
# end def


news_list = []


display = 10
start_values = range(1, 101, display)
sort = 'sim'


news_dataframe = pd.DataFrame()
news_dataframe_summary = pd.DataFrame()
for start in start_values:
    news = news_api(query, display, start, sort)

    lastBuildDate = news["lastBuildDate"]
    total = news["total"]
    start = news["start"]
    display = news["display"]

    items = news["items"]
    for this_news in items:
        title = this_news["title"]
        originallink = this_news["originallink"]
        link = this_news["link"]
        description = this_news["description"]
        pubDate = this_news["pubDate"]

        news_list.append([lastBuildDate, total, start, display, title, originallink, link, description, pubDate])

    columns = ["빌드_날짜", "총_검색결과", "검색_시작", "출력_개수", "뉴스_제목", "원본_URL", "네이버_URL", "뉴스_요약", "게시_날짜"]
    news_dataframe = pd.DataFrame(news_list, columns=columns)

    time.sleep(1)
    news_dataframe_summary = pd.DataFrame([[row[7]] for row in news_list], columns=["뉴스_요약"])

news_dataframe.to_csv(news_filename, index=False, encoding="utf-8-sig")
news_dataframe_summary.to_csv(news_filtered_columns, index=False, encoding="utf-8-sig")
print(news_dataframe['뉴스_요약'])