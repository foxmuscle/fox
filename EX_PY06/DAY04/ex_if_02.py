#------------------------------------------------------
#[실습 ]숫자를 입력 받아서 음이 아닌 정수와  음수 구분하기
#-------------------------------------------------------

num=int(input('숫자 입력:'))

if num >=0 :
    print(f'숫자{num}는 양수 입니다.')
else :
    print(f'숫자{num}는 음수 입니다.')


#---------------------------------------------------------------------
#[실습]점수를 입력 받아서 합격과 불합격 출력
# -합격 :  60점 이상
#---------------------------------------------------------------------
num=int(input('점수입력 :'))

if num >=60 :
    print(f'점수 {num} 합격입니다.!!!')
else :
    print(f'점수 {num} 불합격입니다.!!!')

#----------------------------------------------------------------------
#[실습] 점수를 입력 받아서 학점 출력
# - 학점 : A,B,C,D,F 90 ,80,70,60,50,40
#----------------------------------------------------------------------
num=int(input('점수입력 :'))
if num>=90 :
    print(f'점수 {num} 는 "A" 학점입니다.')
elif  num >=80 :
    print(f'점수 {num} 는 "B" 학점입니다.')
elif num >=70 :
    print(f'점수 {num} 는 "C" 학점입니다.')
elif num >=60 :
    print(f'점수 {num} 는 "D" 학점입니다.')
elif  num >=50 :
    print(f'점수 {num} 는 "E" 학점입니다.')
else :
    print(f'점수 {num} 는 "F" 학점입니다.')  