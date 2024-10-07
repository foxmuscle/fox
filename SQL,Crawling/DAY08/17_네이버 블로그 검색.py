from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote # 한글 검색어 전달에 필요 

query1=quote('챗지피티')# 한글 검색어 전달
query='ChatGPT'
url = f'https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&sm=mtb_jum&query={query}'


html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print('검색 결과수:', len(blog_results))

for blog_title in blog_results:
    title = blog_title.text
    link = blog_title['href']
    print(f'{title},[{link}]')

# 내부의 텍스트 출력
dest_results =soup.select('a.dsc_like')
for desc in  dest_results:
    print(desc.text)
    





html =urlopen(url)
soup=BeautifulSoup(html,f)

for i in range(search_count):
    title =blog_results[i].text
    link = blog_results[i]['href']
    print(f'{title},[{link}]')
    print(desc_results[i].text)
    print('-'*80)