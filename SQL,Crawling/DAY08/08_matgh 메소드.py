# 전화번호 분석
# 전화번호: ‘지역번호-국번-전화번호’
# 전화번호: (2, 3자리)-(3, 4자리)-(4자리)
# 예: 02-123-4567, 053-123-1234
#  groups(): 매칭되는 문자열의 전체 그룹을 리턴

import re
#	^	..	$	을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
match_groups= tel_checker.match('02-123-4567').groups()
print(match_groups)

print(tel_checker.match('053-950-45678'))#마지막 숫자의 자리수가 맞지 않음
print(tel_checker.match('053950-4567'))#dash(-)가 없음

#전화번호에서 dash(-) 제거하고 검사하기-----------------------------

tel_number = '053-950-4567'
tel_number = tel_number.replace('-','')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))#	02-3950-1234



# groups() • 매칭 결과를 튜플로 출력
# group()  • 매칭된 전체 문자열 반환
# group(index) • 해당 인덱스에 매칭된 문자열 반환  • index=0:	전체 리턴


tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m= tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ', m.group())
print('group(0):', m.group(0))
print('group(1):', m.group(1))
print('group(2,3):', m.group(2,3))
print('start():', m.start())	#	매칭된 문자열의 시작 인덱스
print('end():',	m.end())	#	매칭된 문자열의 마지막 인덱스+1


#휴대전화번호
# 휴대전화번호 구성:
#' 사업자번호(3자리)-국번(3,4자리)-전화번호(4자리)’
#  사업자 번호: 010,	011,	016,	017,	018,	019
#  예: 010-123-4567,	011-1234-5678,	019-111-2222


# (?:0|1|[6-9])	의미
# ?:	뒤에 따라 나오는 숫자(0|1|6|7|8|9)를 하나의 그룹으로 합침
cell_phone=ne = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))


















