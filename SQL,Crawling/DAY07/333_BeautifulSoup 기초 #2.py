from bs4 import BeautifulSoup
soup	=BeautifulSoup(html_example,	'html.parser')

print(soup.title)	#	<title>	태그 전체를 가져옴
print(soup.title.string)	#	<title>태그의 텍스트만 리턴
print(soup.title.get_text())	#	.string,	.text(예전 버전)와 동일한 기능
