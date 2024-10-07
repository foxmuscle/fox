#find_all(string=“검색어”)

# 대소문자 구분
# 검색어:‘the	prince’
from	urllib.request	import	urlopen
from	bs4	import	BeautifulSoup


html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup=BeautifulSoup(html,'html.parser')
prince_list =	soup.find_all(string='the	prince')
print(prince_list)
print('the	prince	count:',len(prince_list))