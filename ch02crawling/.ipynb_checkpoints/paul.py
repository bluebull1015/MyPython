
import numpy as np
import pandas as pd
import requests
import folium
import time

from tqdm.notebook import tqdm
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
drive_path = 'chromedriver.exe'
myservice = Service(drive_path)
driver = webdriver.Chrome(service=myservice, options=chrome_options) # 드라이버 객체
print(type(driver))

wait_time = 10
driver.implicitly_wait(wait_time)

#%%
# 폴 바셋 매장 찾기
paulbassett_url = 'https://www.baristapaulbassett.co.kr/store/Store.pb'
driver.get(paulbassett_url) # 해당 페이지로 이동하시오.

time.sleep(1)

# 폴 바셋 '지역' 링크 클릭
paulbassett_local_selector = '#storeLocationEl > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, paulbassett_local_selector))).click()
time.sleep(1)

# 폴 바셋 '서울특별시' 링크 클릭
paulbassett_seoul_selector = '#areaList > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, paulbassett_seoul_selector))).click()
time.sleep(1)

# 폴 바셋 '전체' 링크 클릭
paulbassett_seoul_all_selector = '#countyList > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, paulbassett_seoul_all_selector))).click()


# 폴 바셋 HTML 코드를 파싱하여 html 파일에 기록합니다.
html = driver.page_source
filename = 'paulbassett.html'
htmlFile = open(filename, mode='wt', encoding='UTF-8')
print(html, file=htmlFile)
htmlFile.close()
print(filename + ' 파일 생성됨')

# 파싱된 결과를 BeautifulSoup 객체로 생성합니다.
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
# 파일의 소스를 확인하기 위해 만든 파일(확인 후 삭제해도 됨.)
with open("aa.html", "w", encoding="UTF-8") as file:
    file.write(soup.prettify())

from bs4 import BeautifulSoup
import pandas as pd

# 모든 정보 창 가져오기
shop_list = soup.find_all("ul", class_="src", id="shopList")

# 서울 전체 매장 개수
shop_total_cnt = soup.find("span", id="totalCnt").text

# 데이터를 저장할 리스트


# 매장 정보 추출
shop_items = shop_list[0].find_all("li")  # 모든 <li> 태그 가져오기
data = []
# 반복문 돌릴 전체 매장 개수 가져오기
for shop in tqdm(shop_items):
    name = shop.select_one("strong").text.strip() if shop.select_one("strong") else "이름 없음"
    address = shop.select_one("address").text.strip() if shop.select_one("address") else "주소 없음"
    phone = shop.select_one("dl > dd").text.strip() if shop.select_one("dl > dd") else "전화번호 없음"

    service_dict = {
        '지하철 인접': 'no',
        '주차 가능': 'no',
        '로스팅': 'no',
        '커피 교육': 'no',
        '아이스크림(1FLAVOR)': 'no',
        '아이스크림(2FLAVOR)': 'no',
        '아이스크림(4FLAVOR)': 'no',
        '토핑 아이스크림': 'no',
        '싱글오리진': 'no',
        '딜리버리': 'no',
        '드라이브스루': 'no',
        '피자&파스타': 'no',
        '현금 없는 매장': 'no',
        '밀도': 'no'
    }

paulbassett_seoul_store_selector = f'#mapLayer > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div:nth-child({5}) > img'
WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.CSS_SELECTOR, paulbassett_seoul_store_selector))).click()







# for n in tqdm(range(len(shop_total_cnt))):
#     # 매장 개수 만큼 반목문 돌려서 각 매장 아이콘 정보 가져오기.
#     paulbassett_seoul_store_selector = f'#mapLayer > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div:nth-child({n}) > img'
#     try:
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, paulbassett_seoul_store_selector))).click()
#     except Exception as err:
#         print(f'요소를 찾을 수 없음: {err}')
#     time.sleep(1)





    # 옵션(아이콘) 데이터 가져오기
    # option_area = shop.find("ul", class_="option storeOptionArea")  # 옵션이 있는 ul 찾기
    # if option_area:
    #     option_list = option_area.find_all("li")  # 옵션 리스트(li 태그)
    #     options = [opt.text.strip() for opt in option_list]  # 텍스트만 추출
    # else:
    #     options = ["옵션 없음"]

    # options_text = ", ".join(options)

    # # 2D 리스트에 추가
    # data.append([name, address, phone])
#     print(option_area)

# # 데이터프레임 생성
# df = pd.DataFrame(data, columns=["이름", "주소", "전화번호"])


