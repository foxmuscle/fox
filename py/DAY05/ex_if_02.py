#-----------------------------------------------------------
#===> 1줄로 조건식 을 축약  : 조건부표현식
# -[실습] 문자1개 코드값을 저장하는 조건식을 작성
# -알파벳(a~z,A~Z) 코드값으로 변환
# -그 외의 None으로 코드값으로 전달
#-----------------------------------------------------------

data='m'



# if( ord('a')<=data<=ord('z')) or ( ord('A')<=data<=ord('Z')) :
#     print(data)


if('a'<=data<='z') or ('A'<=data<='Z') :
    print(ord(data))
else :
    print(None)

## 조건부 표현식------------------------------------------------------------------------
print(ord(data)) if ('a'<=data<='z') or ('A'<=data<='Z') else  print(None)

result= ord(data) if ('a'<=data<='z') or('A'<=data<='Z') else (None)
print(f'{data}의 코드값  : {result}')
