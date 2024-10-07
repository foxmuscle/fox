from urllib.request import urlopen
from bs4 import BeautifulSoup


#웹페이지 가지고 오기
html =urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
# print(type(html))
# print(html.read())

# BeautifulSoup 객체 생성
bs=BeautifulSoup(html, 'html.parser')

# print(bs)
# print(bs.h1)  # 웹사이트에서 첫번째 <h1>  태그만 반환
# print(bs.h1.string)

# • 출력 항목 (4개 항목)
# – <p	class=“period-name”>”Overnight”</p>
# – <p	class=“short-desc”>Mostly	Cloudy</p>
# – <p	class=“temp	temp-low”>Low	55	℉	</P>
# – <img class=“…”	title=“Overnight:	Mostly	cloudy,	with	a	low	around	55.	West	southwest	wind	around	13	mph.”	>

#---------------------------------------------------------------------------
# – <p	class=“period-name”>”Overnight”</p>


bsfind=bs.find_all('div', {'class': 'tombstone-container'})



print(bsfind)
print('총개수:', len(bsfind))
















#  2개의 함수를 작성
# • 출력 내용은 동일하지만, 아래 2개의 함수를 각각 구현하시오.
# • def	scraping_use_find(html)
# – find(),	find_all() 함수를 이용하여 스크레이핑
# • def	scraping_use_select(html)
# – select(),	select_one()	함수를 이용하여 스크레이핑


# # tombstone-container 클래스의 모든 요소 찾기
# tombstone_containers = bs.find_all('div', class_='tombstone-container')

# # 총 tombstone-container 개수 출력
# print(f"총 tombstone-container 검색 개수: {len(tombstone_containers)}")

# # 각 tombstone-container에서 정보 추출 및 출력
# for container in tombstone_containers:
#     period = container.find('p', class_='period-name').text
#     short_desc = container.find('p', class_='short-desc').text
#     temp = container.find('p', class_=['temp', 'temp-low', 'temp-high']).text
#     img_desc = container.find('img')['title']
    
#     print("--------------------------------------------------------------------------------")
#     print(f"[Period]: {period}")
#     print(f"[Short desc]: {short_desc}")
#     print(f"[Temperature]: {temp}")
#     print(f"[Image desc]: {img_desc}")

