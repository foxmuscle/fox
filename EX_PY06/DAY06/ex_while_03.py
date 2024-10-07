# #------------------------------
# # 제어문 - while 반복문
# #------------------------------
# ## [실습] 3단 출력하기  while


cnt =0
while cnt<10 :
    print(cnt, f' 3* {cnt} = {cnt*3}')
    cnt=cnt+1

## [실습] 1~30 범위의 수중에서 홀수만 출력
#         while만 사용
 
data=1
while data<31 :
    if data%2:
        print(data)
    data=data+1

data=1
while data<31 :
    print(data)
    data=data+2


for i in range(5) :
    for j in range(5) :
        if  j<= i :
            print('*', end='')
    print()

