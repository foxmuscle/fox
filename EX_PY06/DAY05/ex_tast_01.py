#--------------------------------------------------------------
#[실습] 글자를 입력 받습니다. ==> input()->str
#       입력받은 글자의 (a~z, A~Z)코드 값을 출력 합니다.
#--------------------------------------------------------------
    
data=input('글자 입력 (a~z,A~Z) : ')

#range(문자 많은때 )
#문자 ==> 코드값 변환 내장함수 : ord(문자1개)
if len(data) >0 :  #----->원소의 갯수 확인 부터
    if len(data) ==1: #-----> len으로 문자 가 1개인지 확인 ==
        if 'a'<=data <='z' or 'A'<=data <='Z' :
            print(f'{data} 의 코드값 : {ord(data)}')
        else:('대문자 소문자만 가능합니다')
    
    else:
        ('대문자 소문자만 가능합니다')
    


else :
    print("입력된 데이터가 없습니다. 확인하세요.")

#-----------------------------------------------------------------
if len(data) ==1  and 'a'<=data <='z' or 'A'<=data <='Z' : 
       print(f'{data} 의 코드값 : {ord(data)}')
else : 
    print('1개의 알파벳 문자만 입력해야 합니다. \n 입력된 데이터 확인하세요.')



data='AB'
# ord(data[0])
# ord(data[1])
print(list(map(ord,data)))

#----------------------------------------------------------------

data=input('글자 입력 (a~z,A~Z) : ')

if len(data)and 'a'<=data <='z' or 'A'<=data <='Z' : 
       print(f'{data} 의 코드값 : {ord(data)}')
else : 
    print('1개의 알파벳 문자만 입력해야 합니다. \n 입력된 데이터 확인하세요.')



data='AB'
# ord(data[0])
# ord(data[1])
print(list(map(ord,data)))




#---------------------------------------------------
#[실습] 점수를 입력 받은 후 학점을 출력합니다.
#  - 학점 :A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F
#    A+ :96~100
#    A :95
#    A-:90~94
#---------------------------------------------------

jumsu=int(input('점수 입력해주세요 : '))

if jumsu >=96 :
    print(f' 점수 {jumsu} 점은 A+ 입니다.')
elif jumsu == 95:
    print(f' 점수 {jumsu} 점은 A 입니다.')
elif jumsu >= 90 :
    print(f' 점수 {jumsu} 점은 A- 입니다.')
elif jumsu >= 86 :
    print(f' 점수 {jumsu} 점은 B+ 입니다.')
elif jumsu == 85 :
    print(f' 점수 {jumsu} 점은B 입니다.')
elif jumsu >= 80 :
    print(f' 점수 {jumsu} 점은 B- 입니다.')
elif jumsu >= 76 :
    print(f' 점수 {jumsu} 점은 C+ 입니다.')
elif jumsu == 75 :
    print(f' 점수 {jumsu} 점은 C 입니다.')
elif jumsu >= 70 :
    print(f' 점수 {jumsu} 점은 C- 입니다.')
elif jumsu >= 66 :
    print(f' 점수 {jumsu} 점은D+ 입니다.')
elif jumsu == 65 :
    print(f' 점수 {jumsu} 점은 D 입니다.')
elif jumsu >= 60 :
    print(f' 점수 {jumsu} 점은 D- 입니다.')
else :
    print(f' 점수 {jumsu} 점은 F 입니다.')







junsu=75
grade=''

if jumsu <0 or jumsu >100 : 
    print('{jumsu} 잘못 입력된 점수 입니다.')
else :
    if jumsu >95 :grade="A+"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    elif jumsu == 95 :grade="A"
    
    

    else: grade='F'
 
print(f'{jumsu}는 {grade} 학점입니다.')