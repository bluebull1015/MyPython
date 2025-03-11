# import numpy as np  # 수치 연산 및 배열 처리를 위한 라이브러리
# import pandas as pd  # 데이터 분석 및 DataFrame 처리를 위한 라이브러리
# import requests  # HTTP 요청을 보내고 API 데이터를 가져오는 라이브러리
# import folium  # 지도 시각화를 위한 라이브러리
#
# from tqdm.notebook import tqdm  # 코드 실행 중 진행 상태를 표시하는 진행 바
# from bs4 import BeautifulSoup  # HTML/XML 데이터를 파싱하여 웹 크롤링을 수행하는 라이브러리

from selenium import webdriver  # 웹 브라우저 자동화를 위한 Selenium WebDriver 모듈
from selenium.webdriver.chrome.service import Service  # Chrome WebDriver 실행을 위한 서비스 클래스
# from selenium.webdriver.common.by import By  # 웹 요소를 찾을 때 사용 (id, class, xpath 등)
# from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기하는 기능 제공
# from selenium.webdriver.support import expected_conditions as EC  # 요소의 상태(로딩 완료, 클릭 가능 등)를 정의하는 조건 클래스
import time

# 올바른 ChromeDriver 경로 지정
chrome_driver_path = "D:/MyPython/ch02crawling/chromedriver.exe"

# WebDriver 실행
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# 웹사이트 열기
driver.get("https://www.google.com")














driver.maximize_window()  # 브라우저 창을 최대화





# 스타벅스 매장 찾기
starbucks_url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
driver.get(starbucks_url) #해당 페이지로 이동하시오.