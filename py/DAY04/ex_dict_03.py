#--------------------------------------------------------
#Dict 자료형 살펴보기
# - Dict 자료형 전용의 함수 즉, 메서드(memthod) 사용
# - 사용법 :  변수명.메서드명()
#---------------------------------------------------------
##[Dict 에서 키만 추철하는 제서드 keys()]--------------------
p1={'name':'홍길동', 'age':20, 'jop':'학생'}

result=p1.keys()
print(f' 키 추출 :{result},{type(result)}' )
#error : print(result[0])

# list 형변환=> list(dict_keys타입)
result=list(result)
print(f' 키 추출 :{result},{type(result)}' )

##[Dict 에서 값/데이터만 추출하는 메서드  values()]-----------
result=p1.values()
print(f' 키 추출 :{result},{type(result)}' )



##[Dict 에서 키와 값을 묶어서 추출하는 메서드  items()]----------
result=p1.items()
print(f' 키 추출 :{result},{type(result)}' )

result=list(result)
print(f' 키 추출 :{result[0]},{type(result[0])}' )
