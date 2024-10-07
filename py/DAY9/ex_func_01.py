#--------------------------------------------------------
# 함수(Function)이해 및 활용
#--------------------------------------------------------
# 함수 기능 : 3개의 정수를 덧셈 후 결과를 반환하는 함수
# 함수 이름 : add3
# 매개 변수 : num1,num2,num3
# 함수 결과 : 정수 result
#---------------------------------------------------------

def add3(num1,num2,num3) :
    result=num1+num2+num3
    return result


#--------------------------------------------------------
# 함수(Function)이해 및 활용
#--------------------------------------------------------
# 함수 기능 : 3개의 정수를 곱셈한 후 결과를 반환하는 함수
# 함수 이름 : multi3
# 매개 변수 : num1,num2,num3
# 함수 결과 : 정수 result
#---------------------------------------------------------

def multi(num1,num2,num3) :
    result=num1*num2*num3
    return result


#--------------------------------------------------------
# 함수(Function)이해 및 활용
#--------------------------------------------------------
# 함수 기능 : 개의 정수를 나눗셈한 후 결과를 출력하는 함수
# 함수 이름 : div
# 매개 변수 : num1,num2
# 함수 결과 : None
#---------------------------------------------------------

def div (num1,num2) :
    if not num2 : #not 0  -->True
        result='0으로 나눌수 없음'
    else :
        result=num1/num2
    print(f'{num1}/{num2}={result}')



#함수 사용하기 즉 , 호출----------------------------------
## 덧셈하기


value=add3(1,2,3)


# 나눗셈하기
value1=div(3,4)
print(value1)



#-------------------------------------------------------
#함수(Function)이해 및 활용
#함수 기반 계산기 프로그램
# - 4칙연산 기능별 함수 생성 => 덧셈 ,뺄셈 ,곱셈, 나숫셈
# - 2개  정수만 계산
#-------------------------------------------------------



def add2(num1,num2) :
    result=num1+num2
    return result

def add (num1,num2):
    return a+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2) :
    return num1*num2

def divide(num1,bnum2):
    if num2 ==0 :
        return "0"
    else :
        return num1/num2
    

## 계산기 프로그램-------------------
# - 사용자가 종료를 원할때 종료  => 'x','X'입력시
# - 연산방식과 숫자 데이터 입력받기
#------------------------------------------------------------------------------
while True :
    # (1) 입력 받기
    req =input('연산( +,-,*,/)방식과 정수 2개 입력(예: + 10 2): ')
    #(2) 종료 조건 검사
    if req =='x'or req =='X':
        print('계산기를 종류 합니다.')
        break
    #(3) 입력에 대한 연산 방식과 데이터 추출 '+ 10 2'
    op, num1, num2 = req.split() #["+","10","2"]
    #str 정수 ==> int 변환
    num1=int(num1)
    num2=int(num2)
    #연산 방식에 따라서 계산 진행
    if op=='+' :
        print(f'{num1} + {num2}={add(num1,num2)}')

    elif op=='-' :
        print(f'{num1} - {num2}={subtract(num1,num2)}')

    elif op=='*' :
        print(f'{num1} * {num2}={multiply(num1,num2)}')

    elif op=='/' :
        print(f'{num1} / {num2}={divide(num1,num2)}')





while True:
    # (1) 입력 받기
    req=input('연산(+,-,*,/)방식과 정수 2개 입력(예: + 10 2)')
    # (2) 종료 조건 검사
    if req=='x' or req=='X':
        print('계산기를 종료합니다.')
        break
    # (3) 입력에 연산방시과 데이터 추출
    op, num1, num2 = req.split()  # ['+', '10','2']
    # str 정수 ==> int 변환
    num1=int(num1)
    num2=int(num2)
    # 연산방식에 따라서 계산 진행
    if op=='+':
        print(f'{num1}+{num2}={add(num1,num2)}')
    elif op=='-':
        print(f'{num1}+{num2}={sub(num1,num2)}')
    elif op=='*':
        print(f'{num1}+{num2}={mul(num1,num2)}') 
    elif op=='/':
        print(f'{num1}+{num2}={div(num1,num2)}')  