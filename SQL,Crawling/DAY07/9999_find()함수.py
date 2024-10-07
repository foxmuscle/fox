


# p.13
href_value =soup.find(attrs={'href'	:	'www.google.com'})
href_value =soup.find('a',	attrs={'href':	'www.google.com'})
print('href_value:	',	href_value)
print(href_value['href'])
print(href_value.string)

# BeautifulSoup 기초: find()함수.

#  find()	함수
# • span 태그의 속성 가져오기

span_tag =	soup.find('span')
print('span	tag:',	span_tag)
print('attrs:',	span_tag.attrs)
print('value:',	span_tag.attrs['class'])
print('text:',	span_tag.text)



# BeautifulSoup 기초: find_all() 함수-----------------------
links	=	soup.find_all('a')
for	alink in	links:
				print(alink)
				print(f"url: {alink['href']},	text:	{alink.string}")
				print()
				
#BeautifulSoup 기초: find_all() 함수---------------

# 특정 태그 중 여러 속성값을 한 번에 검색
link_tags =	soup.find_all('a',	{'class':['external_link',	'internal_link']})
print(link_tags)

#<p>태그의 id값이 ‘first’,	‘third’인 항목 검색
p_tags =	soup.find_all('p',	{'id':['first',	'third']})
for	p in p_tags:
        print(p)


 #select_one() 함수 예제-  <h1>태그의 id	검색: #id

 #	<h1>태그의 id가 "footer＂인 항목 추출
footer	=	soup.select_one('h1#footer')
print(footer)

 #클래스 이름 검색: 태그.클래스이름 – <a class=“internal_link”	herf=“/pages/page1.html>Page1</a> 검색

class_link =	soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])

  
#BeautifulSoup 기초: select_one() 함수 P24

 #계층적 하위 태그 접근 #1 -• (부모태그 > 자식태그) 형식으로 접근:	태그가 단계적으로 존재할 때
 
 #계층접근
like1=suup.select_one('div#like > a.external_like')
print(like1)


#find() 함수와 비교
link_find= soup.find('div',{'id' : 'like'})

external_link =	link_find.find('a',	{'class':	'external_link'})
print('find	external_link:	',	external_link)



#p25
#third_tag ==>internal_like 바꾸기
#p26

h1_all =soup.select('h1')
print('h1_all :',h1_all)

url_links = soup.select('a)')
for link in url_links:
        print(link['href'])