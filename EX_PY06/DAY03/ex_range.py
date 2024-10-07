#------------------------------------------------------------
# 내장함수  ramge()
# - 숫자 범위를 생성하는 내장함수
# - 형식 : range(시작하는 함수,끝나는 함수+1)
#          range(끝숫자 +1)
#------------------------------------------------------------
#1~100숫자를 저장하세요
nums=range(1,101)

print(f'nums 값 : {nums}\n타입  : {type(nums)}\n 개수 :len(nums)') 

print()

#원소 /요소 읽기==> 인덱싱
print(nums[0],nums[-1])
# 원소 요소 여러개 읽기 ==> 슬라이싱
print(nums[0:10],nums[30:41])
# 원소 /요소 하나하나를 보기 ==> list/tuple 형변환
print(list(nums[0:10]),tuple(nums[30:41]))


# [실습1] 1~100 에서 3의 배수만 저장하세요 
# => 3,6,9,12,.......,99
#three=[3,6,9,12,15,18,21......,99]
three=range(3,101,3)
print(list(three))
print(three)


# [실습2] 1.0~10.0 사이에 숫자 저장
datas=list(range(1,11))
print(datas)
#====>하나하나 float 로 바꾸면 힘드니깐..==> map() 내장함수
#map ==>

datas=(map(float,datas))
print(datas) #??????
datas=list(map(float,datas))
print(datas)