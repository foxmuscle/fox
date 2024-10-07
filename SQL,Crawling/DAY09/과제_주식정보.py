from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium.webdriver.common.by import By


import	collections
if	not	hasattr(collections,	'Callable'):
    collections.Callable =	collections.abc.Callable




url='https://finance.naver.com/sise/sise_market_sum.naver'

html=requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

tltle = soup.select('a.tltle')
#         find_all('a',{'class':'tltle'})
# print(tltle)

text_list=[]
url_list=[]


for i in tltle[:10]:
    text_list.append(i.text)
    url_list.append(i.attrs['href'])    


for u in url_list :
    href=f'https://finance.naver.com/{u}'
    


# print(html.read())

# § 프로그램 동작 • 코스피 상위 10
# 개 기업의 URL
# 및 기업 이름을 리스트에 저장
# • 메뉴에서 선택한 기업의 세부 주식 정보를 화면에 출력 • 사용자가 -1을 입력할 때 까지 계속 반복함

# 상위 10개 기업 정보 저장
# companies = []




































