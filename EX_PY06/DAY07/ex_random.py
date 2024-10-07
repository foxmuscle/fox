 #---------------------------------------------
# 모듈 : 변수 ,함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은
#       여러게 모듈 파일들 존재
# 모듈 사용법  :  import 모듈파일명   <-------- 확장자 제외
#----------------------------------------------------------
import  random as rad

#random.random()

rad.random()

# 임의의 숫자를 생성 추출하기 ------------------------------
# 임의의 숫자 10개 생성---------------------



rad.random()

for cnt in range(10):
    print(rad.random()*10)


# -> 0.0 <= ~ <1.0
for cnt in range(10):
    print(int(rad.random()*10)) 

#-> randint(a,b) : a<= ~ <=b
for cnt in range(10):
    print(rad.randint(0,1))


#-------------------------------------------
#[실습] 로또 프로그램을 만들어주세요 
# - 1~45 범위에서 중복되지 않는 6개 추출
#-------------------------------------------
## -반복의 횟수 ? 알수 없음  => 반복횟수가 있음 whle  for 결정
## -무한반복문
## -종료조건? 중복 x 6 개 숫자==>list ,set, dict


lotto=[0,0,0,0,0,0]
idx=0
while True :
    num = rad.randint(1,45)
    if num not in lotto: 
        lotto[idx]= num 
        idx=idx+1
    if idx ==6 : break
print(lotto)


lotto={}
key=1
while len(lotto)< 6:
    num = rad.randint(1,45)
    if num not in lotto.values() :
        lotto[key]= num 
        kky=key+1
    if key ==6 : break  #--> len 쓰면 없어짐
print(lotto.values())



lotto=set()
key=1
while True :  
    num = rad.randint(1,45)
    num_set=set([num])
    lotto=lotto.union(num_set)

print(lotto)



#-----------------------------------------------

#set  타입의 add()메서드
lotto=set()
while len(lotto)<6:
    num = red.ramdint(1,45)
    lotto.add(num)
print(looto)






#------------------------------------

# import random

# def generate_lotto_numbers():
#     # 1부터 45까지의 숫자 중에서 6개를 선택하여 반환하는 함수
#     numbers = random.sample(range(1, 46), 6)
#     numbers.sort()
#     return numbers

# def main():
#     print("로또 추첨을 시작합니다!")
#     num_games = int(input("몇 줄을 구매하시겠습니까? "))
    
#     for _ in range(num_games):
#         numbers = generate_lotto_numbers()
#         print(numbers)
    
#     print("로또 추첨을 종료합니다.")

# if __name__ == "__main__":
#     main()


















