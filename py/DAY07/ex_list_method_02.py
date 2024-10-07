#----------------------------------------
# 리스트 전용의 함수, 즉 메서드 (methed)
# -리스트의 원소 요소 를 제어 하기 위한 함수
#---------------------------------------



# 메서드 요소추가 메서드 append(데이터)-----------------------
datas=[1,3,5]
# 새로운 데이터 100추가  : 제일 마지막 원소 추가 
datas.append(100)
print(f'datas 개수 :{len (datas),{datas}}')

datas.append(100)
print(f'datas 개수 :{len (datas),{datas}}')





# 메서드 - 요소추가 메서드 insert(인덱스 ,데이터)]----------------

datas.insert(0,300)
print(f'datas 개수 :{len (datas),{datas}}')

datas.insert(-1,300)
print(f'datas 개수 :{len (datas),{datas}}')



# [실습]: 임의의 정수 숫자 10개 저장하는 리스트 생성]]----------------
# -random 모듈
# -빈리스트 생성
# -for   반복문



import random as red

nums=[]

for cnu in range(10):
    n=red.randint(1,50)
    nums.append(n)

print(f'nums=> {nums}')



for cnu in range(10):
     nums.append(red.randint(1,50))# ===> 굳이 딴곳에 안쓰면 저장 안하고  바로 넣으면 됨

print(f'nums=> {nums}')  




#[ 메서드 - 요소 삭제 메서드 remove(인덱스 ,데이터)]-------------
# 존재하지 않는 데이터 삭제 시 ERROR 발행함!!


for cnt in range(datas.count(300)):
    datas.remove(300)
    print(f'datas 개수 : {len(datas)},{datas}')




