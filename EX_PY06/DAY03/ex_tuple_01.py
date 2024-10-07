#------------------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
# - 다양한 종류의 여러 개 데이터를 저장하는 타입
# - List 와 비슷하지만 수정, 삭제 안됨!!
# - 형식  : (데1,.....,데n)
#           데,....,데n
#            (데,) 또는 데,
#----------------------------------------------------------------
# 튜플 데이터 생성

datas=()
print(type(datas),datas ,len(datas))

datas=(1,5,7)
print(type(datas),datas ,len(datas))

datas=(1,)
print(type(datas),datas ,len(datas))

datas=1,
print(type(datas),datas ,len(datas))

# 튜플 데이터의 원소/요소 읽기----------------------------------
datas=11,22,33,44,55
#      0  1  2  3  4
#     -5 -4 -3 -2 -1

#2번요소 읽기
print(datas[2],datas[-3])

#1,2,3 번 요소 읽기
print(datas[1:4])

#요소/원소 수정 및 삭제 즉 ,변경 불가!!
#datas=11,22,33,44,55
#마지막 원소를 'A'로 변경
  
#datas[-1]='A'  -> 안됨

# 마지작 원소를 삭제해줘
del datas[-1]

# 튜플 데이터의 원소/요소 변경 ==> 형변환-----------------------------
birthday=(2024,1,1)
#1월 ==> 3월 변경
birthday=list(birthday)
birthday[1]=3

#list ==> Tuple 형변환
birthday=tuple(birthday)
