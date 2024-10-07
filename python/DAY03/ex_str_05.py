#----------------------------------------------------------------
# 문자열 str 데이터 나누기
# - 이스케이프문자 : 특수한 의미를 가지는 문자
# *형식: \문자1개
#       '\n' -줄바꿈 문자
#       '\t'-탭간격 문자
#       '\''-홑따옴표 문자
#       '\"'-쌍따옴표 문자
#       '\\'-\ 백슬러지 문자,경로 (path) ,url관련
#       '\U' -유니코드
#       '\a'-
#-------------------------------------------------------------------
msg='오늘은 좋은날\n내일은\n주말이라\n행복해'
print(f"msg 줄바꿈 : {msg}")

msg="오늘은 나의 \'생일\' 이야"
print(msg)

msg='오늘은 나의 \"생일\" 이야'
print(msg)

#r' ' 또는 R' '  : 문자열 내 이스케이프 문자는 무시됨!
file='C:\\Users\\LG\\.continuum\\anaconda-client\\test.txt'
print(file)

file=r'C:\Users\LG\.continuum\anaconda-client\test.txt'
print(file)

msg="Happy\tnew\tyear"
msg2=R"Happy\tnew\tyear"

print(msg)
print(msg2)