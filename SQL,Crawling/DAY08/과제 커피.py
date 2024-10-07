from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('https://www.hollys.co.kr/')

# BeautifulSoup 객체 생성
bs=BeautifulSoup(html, 'html.parser')


print(bs.prettify()) 
print(len('td'))

#1~50장
start_page = 1
end_page = 50
#1~50페이지
for page in range(start_page, end_page + 1):
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="