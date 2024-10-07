#정규 표현식 객체 사용:	
# 정규식 객체를 생성: compile(pattern)
# 동일 패턴을 여러 번 검색하는 경우, 편리하게 사용
# re모듈 함수들은 pattern 파라미터 없이 호출이 가능
# search(string,	pos),	match(string,	pos) 등


import re

#	compile()	사용 안함-------------------------------
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I	like apple!'))
#-->정규식 객체 생성 안함->매번 패턴 입력 (소문자)

# compile() 사용: 객체 생성-----------------------
p = re.compile('[a-z]+') #	알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I	like	apple	123'))

#-->정규식 객체(p) 생성- 알파벳 소문자 패턴- 여러 번 사용


# match():	문자열의 처음부터 검사-----------------------------
m =	re.match('[a-z]+',	'pythoN') #	소문자가 1개 이상
print(m)

m = re.match('[a-z]+',	'PYthon')	#	소문자가 1개 이상
print(m)



#<re.Match object;	span=(0,	5),	match='regex’>
print(re.match('[a-z]+',	'regex	python'))

# None	# 문자열 처음에 공백 포함
print(re.match('[a-z]+',	'	regexpython'))

#<re.Match object;	span=(0,	10),	match='regexpytho’>	
print(re.match('[a-z]+',	'regexpythoN'))

#None	 # $: 문자열의 마지막에 소문자 1회 이상 검사
print(re.match('[a-z]+$',	'regexpythoN'))

#<re.Match object;	span=(0,	5),	match='regex’>	
print(re.match('[a-z]+',	'regexPython'))

#<re.Match object;	span=(0,	11),	match='regexpython'>
print(re.match('[a-z]+$',	'regexpython'))



#정규 표현식 예제 #3-----------------------------§
#  findall() 함수--- 일치하는 모든 문자열을 리스트로 리턴--

p= re.compile('[a-z]+')#	알파벳 소문자

print(p.findall('life	is	too	short!	Regular expression	test'))


#search()	함수-  일치하는 첫 번째 문자열만 리턴--------

result = p.serch('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)