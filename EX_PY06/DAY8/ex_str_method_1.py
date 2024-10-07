#--------------------------------------------------------------
# str 데이터 타입 전용 함수 즉 메서드 살펴보기
#--------------------------------------------------------------

msg='Hello 0705'

#[원소 /요소 인덱스 찾기 메서드 ]- find(문자1개 또는 문자열)]------------------------------

# -'H' 의 인덱스
idx=msg.find('H')
print(f'H 의 인덱스 : {idx}')

# -  '7' 의 인덱스
idx=msg.find('7')
print(f'7 의 인덱스 : {idx}')


# -  'llo' 의 인덱스
idx=msg.find('llo')
print(f'llo 의 인덱스 : {idx}')


# -  'llO' 의 인덱스 --> 대소문자 일치, 존재하지 않으면 -1 결과
idx=msg.find('llO')
print(f'llO 의 인덱스 : {idx}')

#[원소 /요소 인덱스 찾기 메서드 ]- index(문자1개 또는 문자열)]----------------------------
# - 'H' 의 인덱스

idx=msg.index('H')
print(f'H의  인덱스 : {idx}')


# - 'h'  의 인덱스 : 존재하지 않으면 Error 발생
if 'h' in msg :

    idx=msg.index('h')
    print(f'h의  인덱스 : {idx}')

else :
    print('h는 존재 하지 않습니다.')

#----------------------------------------------------------
# 문자열에 동일한 문자가  여러개 존재하는 경우
#----------------------------------------------------------
msg="Good Luck Good"



cnt=msg.count('o')
print( f'cnt=>{cnt}')

for n in range(cnt):
    idx= msg.find('o',idx+1)
    print(f' {n} 번째 o의 인덱스 : {idx}')

# # - 'o' 의 인덱스 찾기 =>  첫번째 'o' 인덱스
# idx= msg.find('o',0)
# print(f' o의 인덱스  : {idx}')

# # - 'o' 의 인덱스 찾기 =>  두번째 'o' 인덱스
# #--------- "od Luck Good"

# idx= msg.find('o',idx+1)
# print(f' o의 인덱스  : {idx}')

# # - 'o' 의 인덱스 찾기 =>  세번째 'o' 인덱스
# #--------- "d Luck Good"

# idx= msg.find('o',idx+1)
# print(f' o의 인덱스  : {idx}')


# # - 'o' 의 인덱스 찾기 =>  네번째 'o' 인덱스
# #--------- "d Luck Good"

# idx= msg.find('o',idx+1)
# print(f' o의 인덱스  : {idx}')

#--------------------------------------------------------------
# 문자열의 뒷부분부터 찾기하는 메서드 ===> rfind(문자,시작인덱스, 끝인덱스+1), rindex(문자,시작인덱스, 끝인덱스+1)
#--------------------------------------------------------------
msg = "happy"

#-첫번째'p'인덱스 찾기
#"happy"
idx=msg.rfind('p')
print(f'p의 인덱스 : {idx}')


#-두번째'p'인덱스 찾기 
#"happy"
idx=msg.rfind('p',0,idx)
print(f'p의 인덱스 : {idx}')


#- 파일명에서 확장자 txt ,jpeg ,xlsx ,zip,gz 찾기
# -hello.txt

files= ['hello.txt', '2024년 상반기경경제분석.doc', 'kakao_12345566879.jpg' ]


for file in files:
    #'.' 인덱스 찾기
    dot=file.find('.')
    #str에서 확장자만 출력
    print(file[dot+1:])










