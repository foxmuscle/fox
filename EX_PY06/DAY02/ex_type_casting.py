#------------------------------------------------------------------------
# 형변환 / 타입캐스팅
# -자료형을 다른 종류의 자료형으로 변경
# - 종류
# * 자동/ 묵시적 형변환 : 컴퓨터가 진행
# * 수동/ 명시적 형변환 : 개발자가 진행
#------------------------------------------------------------------------


age=20.7
 #float----> int변환 : 다시저장하지 않으면 형변환 결과 적용X 

print(age, int(age))
print(age)

age=int(age)
print(age)
print(age,type(age))
#정수를int -----> 실수로float

age= float(age)
print(age)
print(age,type(age))


#float--->str 변환
age=str(age)
print(age)
print(age,type(age))