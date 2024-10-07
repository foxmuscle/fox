#----------------------------------------------
#[실습] 데이터 저장 및 변수 생성 그리고 출력
# - 생년원일
# - 띠( 용.범)
# - 혈액형
# - 출력형태 
# 나는 0000년 00월 00 일00띠 입니다
# 혈액형은 단무지 o형입니다.

y=2024
m=12
day=0
c_z='양띠'

blood='O'
print(f'나는{y}년 {m}월 {day}일 {c_z} 입니다.')


print(f'혈액형은 단무지인 {blood}형 입니다.')

#-----------------------------------------------
# [실습2]입력받은 데이터 저장 단.파일로
# - 좋아하는 계절
# - 좋아하는 나라 
# - 여행가고 싶은 나라

a=input('좋아하는 계절?')

b=input('좋아하는 나라?')

c=input('여행가고 싶은 나라?')


FILENAME='info.txt'

f=open(FILENAME, mode= 'w', encoding='utf-8')
f.write(a)
f.write('\n')#줄바꿈 문자
f.write(b)
f.write('\n')#줄바꿈 문자
f.write(c)

print(f'좋아하는 계절 : {a}, file=f')


f.close()











# FILENAME='result.txt'
# # 파일을 쓰기 모드(w) 열기
# f=open(FILENAME, mode= 'w')
# #f.write("hello")
# # 파일에 데이터 출력하기
# print( "good luck ", file=f)
# #파일 닫기
# f.close()