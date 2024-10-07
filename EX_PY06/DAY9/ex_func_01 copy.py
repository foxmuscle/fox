
#-------------------------------------------------------
#함수(Function)이해 및 활용
#함수 기반 계산기 프로그램
# - 4칙연산 기능별 함수 생성 => 덧셈 ,뺄셈 ,곱셈, 나숫셈
# - 2개  정수만 계산
#-------------------------------------------------------



# def add2(num1,num2) :
#     result=num1+num2
#     return result

def add (num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2) :
    return num1*num2

# def divide(num1,num2):
#     if num2 ==0 :
#         return "0으로 나눌수 없"
#     else :
#         return num1/num2
#-----------------------------------------------------------------
# 함수 기능 : 계산기 메뉴를 출력하는 함수
# 함수 이름 : print_menu
# 매개 변수 : 없음
# 함수 결과 : 없음
#-----------------------------------------------------------------
def print_menu() :
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"*  1.덧  셈  *":16}')
    print(f'{"*  2.뺄  셈  *":16}')
    print(f'{"*  3.곱  셈  *":16}')
    print(f'{"*  4.나눗셈  *":16}')
    print(f'{"*  5.종  료  *":16}')
    print(f'{"*":*^16}')
    


print_menu()

#-----------------------------------------------------------------
# 함수 기능 : 연산 수행 후 결과를 반환하는 함수
# 함수 이름 : calc
# 매개 변수 : 함수명,str 숫자2개
# 함수 결과 : 없음
#-----------------------------

def calc (func,num1,num2,op):
    num1=int(num1)
    num2=int(num2)
    print(f'결과 :{num1}{op}{num2} {func(num1,num2)}')




# print(f'{"*":^16}') # 가운데 정렬
# print(f'{"*":>16}') # 오른쪽 정렬
# print(f'{"*":<16}') # 왼쪽 정렬

# print(f'{"*":*^16}') # 가운데 정렬
# print(f'{"*":*>16}') # 오른쪽 정렬
# print(f'{"*":*<16}') # 왼쪽 정렬





## 계산기 프로그램--------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택시 프로그램 종료
# #=> 반복 =>무한 반복 :While
#------------------------------------------------------------------------------
while True :
    #메뉴출력
    print_menu()

    #메뉴 선택 요청
    # choice = int(input("메뉴 선택"))

    choice = input('메뉴선택:')
    if choice.isdecimal():
        choice=int(choice)
    else: 
        print(('0~10숫자만 입력하세요 .'))
        continue

    #종료 조건 (5번 메뉴 선탣) 처리
    if choice ==5 :
        print("프로그램을 종료합니다.")
        break
    elif choice == 1: # 덧셈
        print("덧셈")
        num1,num2 =input("정수 2개 (예:10,2):").split()
        num1=int(num1)
        num2=int(num2)
        print(f'==>결과{num1}+{num2}= {add (num1,num2)}')

    elif choice == 2: # 뺄셈
        print("뺄셈")
        num1,num2 =input("정수 2개 (예:10,2):").split()
        calc (subtract,num1,num2,'-')
       

    elif choice == 3: # 곱셈
        print("곱셈")
        num1,num2 =input("정수 2개 (예:10,2):").split()
        calc (multiply ,num1,num2,'*')

    elif choice == 4: # 나눗셈 
        print("나눗셈")

    else:
        print('선택된 메뉴가 없습니다.')

    