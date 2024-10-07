
# § URL	구조
# • scheme:	‘http’	또는 ‘https’
# – ftp,	file,	gopher,	mms,	news,	nntp,	sftp,	telnet 등
# • netloc:	인터넷 주소
# § urllib.urlparse
# • 파이썬 표준 라이브러리
# • HTTP요청, 파싱과 관련된 패키지

from urllib.parse import urlparse

urlString1 ='https://shopping.naver.com/home/p/index.naver'

url =	urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)