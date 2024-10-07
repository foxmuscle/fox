#--------------------------------------------
# 리스트 전용의  함수 즉 메서드 (method)
# - 리스트 원소/ 요소를 제어 하기 위한 함수들
#----------------------------------------------
import  random as rad
#[1] 실습 데이터 -> 임의의 정수 숫자 10개 구성된 리스트 

datas=[1,2,3,4,5,3,7,8,3,10]

# [메서드 - 요소 인덱스를 반환하는 메서드 index(데이터 , 찾기시작인덱스)]
# -> 11의 인덱스 찾기
# -> 왼쪽 >>>>> 오른쪽으로 찾기

idx=datas.index(8)
print(f'11의 인덱스 : {idx}')

#-> 0의 인덱스를 찾기 ==> 존재하지 않는 데이터의 경우 ERROR
if 0 in datas :
    idx=datas.index(11)
    print(f'11의 인덱스 : {idx}')
else :
    print('0 은 존재하지 않는 데이터 입니다.')


# -> 3의 인덱스 찾기

if 3 in datas:
    idx=datas.index(3) 
    print(f'첫번째 3의 인덱스 : {idx}')


    idx=datas.index(3,idx+1) 
    print(f'두번째 3의 인덱스 : {idx}')


    idx=datas.index(3,idx+1) 
    print(f'세번째 3의 인덱스 : {idx}')

#[메서드 - 데이터가 몇개 존재하는지 갯수 파악하는 메서드 count(데이터)--------]

cnt=datas.count(3)
print( f' 3 의 개수  : {cnt}')

idx=0
for i in range(cnt):
    idx=datas.index(3,idx if not i else idx+1)
    print(f'{i+1} 번째 3의 인덱스 : {idx}')