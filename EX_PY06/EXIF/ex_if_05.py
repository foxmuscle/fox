#-----------------------------------------------------
#  숫자를 입력 받아서 0이상이면 큰 숫자라면 
# 해당 숫자가 홀수인지 짝수 인지 검사를 하고 
# 0미만이면 '잘못된 숫자'라고 출력 해주세요 
#-----------------------------------------------------

num=input('숫자 입력해주세요  :')


if len(num)==1:
    if '0'<=num<'9' :
        num=int(num)
        if num >=0: 
            if num%2==0 :
                print(' 짝수')
            else:
                print('홀수')

        else :
            print('잘못된 숫자')

    else: 
        print('잘못입력.')
else:
    print('숫자만 입력 가능')

# if num<0 :
#     print('잘못된 숫자')
# else :
#     if num%2==0 :
#         print(' 짝수')
#     else:
#         print('홀수')



if len(num)==1:
    if '0'<=num<'9' :
        num=int(num)
        if num >=0: 
           print(' 짝수')if num%2==0 else  print('홀수')
        else :
            print('잘못된 숫자')
    else: 
        print('숫자만 입력.')
else:
    print('입력된것이 없거나 2개 이상 입력')
