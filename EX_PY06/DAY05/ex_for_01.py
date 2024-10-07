#-----------------------------------------------------------
# 제어문 -반복문 
# - 유사하거나 동일한 코드를 1번 작성으로 재사용하기 위한 방법
# - 종류 : for, while
#-----------------------------------------------------------
## for 반복문
## -시퀀스 (이터러블) 데이터에서 원소/요소를 하나씩 읽어올때 사용
## -형식
## -for 변수명 in 시퀀스 / 이터러블데이터 :
## ----반복실행될 코드
#------------------------------------------------------------
#[실습] 문자열에서 문자를 한줄에 1개씩 줄력하기
msg='Merry Christmas 2025'
#   m=m[0]
for m in msg :
    print(m, ord(m),end=' ')

print('end')

#[실습] 리스트에서 원소를 하나씩 읽어오기-------------------------
#1~100 범위에서 3의 배수만 저장한 리스트
data=list(range(3,101,3))

for d in data :
    print(d,end=' ')


print("END")

# [실습] str 타입의 원소를 가지는 리스트 입니다.
# 해당 원소를 정수로 형변환 시켜서 저장해주세요 
# 원래 원소의 값을 변경해야 하는 경우는 인덱스 필요!!!!!!!!
# -원소의 개수 -> 인덱스 볌위 를 알수 있음

data = ['4','9','1','3','8']

data[0]=int(data[0])

for d in data :
    int(d)

# 리스트의 인덱스 가져 오기
for idx in range(len(data)) :
    print(f'idx => {idx}')
    data[idx]=int(data[idx])

print('후',data)
