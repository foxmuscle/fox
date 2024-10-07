from	urllib.request import	urlopen
html	=	urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())



from urllib.request	import	urlopen
from bs4	import	BeautifulSoup
html =	urlopen('http://www.pythonscraping.com/pages/page1.html')
bs	=	BeautifulSoup(html.read(),	'html.parser')
print(bs)
print(bs.h1)
print(bs.h1.string)	#	.string:	태그 내부의 문자열만 가져옴

#신뢰할 수 있는 연결과 예외 처리
#  예외 처리
# • 페이지를 찾을 수 없는 경우
# – 404	Page	Not	Found 에러 발생:	HTTPError 예외 발생 시킴
# • 서버를 찾을 수 없는 경우
# – 500	Internal	Server	Error		발생시 URLError 예외 발생 시킴
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html =	urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The	server could not be found!')
else:
    print('It worked!')

# 신뢰할 수 있는 연결과 예외 처리----------------------------------------

#  존재하지 않는 태그 접근
# • None	객체 반환
# • None 객체에 접근: AttributeError 발생

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url ,tag):
    try:
        html = urlopen(url)
    except HTTPError as e :
        return None
    

    try:
        bsObj =	BeautifulSoup(html.read(),	'html.parser')
        value	=	bsObj.body.find(tag)
    except	AttributeError as	e:
        return	None	
    return	value

tag='h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html',	tag)
if	value	==	None:
    print(f'{tag} could	not	be	found')
else:
    print(value)

# requests 모듈 사용 예제------------------------------------------

import	requests
from	bs4	import	BeautifulSoup
url =	'http://www.pythonscraping.com/pages/page1.html'
html	=	requests.get(url)
print('html.encoding:',	html.encoding)
print(html.text)
soup	=	BeautifulSoup(html.text,	'html.parser')
print()
print('h1.string:',	soup.h1.string)

# urllib.request.Request 클래스-----------------------------------

# 멜론 웹사이트 접근 #1-------------------------

from urllib.request	import	urlopen
from bs4	import	BeautifulSoup
#	샘플 코드 1
#	urllib.error.HTTPError:	HTTP	Error	406:	Not	Acceptable	발생
melon_url =	'https://www.melon.com/chart/index.htm'
html=urlopen(melon_url)
soup=BeautifulSoup(html.read(),	'html.parser')
print(soup)


# 멜론 웹사이트 접근 #2--------------------------------------
from	urllib.request	import	urlopen
from	urllib.request	import	Request
from	bs4	import	BeautifulSoup
melon_url =	'https://www.melon.com/chart/index.htm'
#	HTTP	request	패킷 생성:	Request()
urlrequest =	Request(melon_url,	headers={'User-Agent':'Mozilla/5.0'})
html	=	urlopen(urlrequest)
soup	=	BeautifulSoup(html.read().decode('utf-8'),	'html.parser')
print(soup)


# User-Agent 사용 비교: urllib.request, requests

from	urllib.request	import	urlopen
from	urllib.request	import	Request
from	bs4	import	BeautifulSoup
import	requests
def	use_urlopen(url):
				#	HTTP	request	패킷 생성:	Request()
				urlrequest =	Request(url,	headers={'User-Agent':	'Mozilla/5.0'})
				html	=	urlopen(urlrequest)
				soup	=	BeautifulSoup(html.read().decode('utf-8'),	'html.parser')
				print(soup)
def	use_requests(url):
				response	=	requests.get(url,	headers={'User-Agent':	'Mozilla/5.0'})
				soup	=	BeautifulSoup(response.text,	'html.parser')
				#print(soup.text)
				print(soup)