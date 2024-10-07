#-----------------------------------------------------------
# 제어문 - 반복문
#-----------------------------------------------------------
#[실습] 출력하고 싶은 단을 입력 받아서 
#      해당 단의 구구단을 출력하세요 
# [출력 예식] 2*1=2
dan=2
n=range(1,10)
for nn in n :
    # print(nn)
    # print(nn*2)
    print(f'{dan}*{nn}= {dan* nn}')


for n in range(1,10):
    print(f'{dan}*{n} ={dan*n}')




dan=3
nums=[1,2,3,4,5,6,7,8,9]
for n in nums :
    print(f'{dan}*{n}= {dan*n}')



a=['1','2']
for n in a :
    print(type(int(n)))



print(f'{dan}* 1 = {dan*1}')
print(f'{dan}* 2 = {dan*2}')
print(f'{dan}* 3 = {dan*3}')
print(f'{dan}* 4 = {dan*4}')
