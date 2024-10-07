#--------------------------------------------------------
# Dict 자료형 살펴보기
# -연산자와 내장함수 
#---------------------------------------------------------
dog={'name':'홍길동', 'age':20, 'jop':'학생'}

person={'age' : 1,'gendar' : '여 ','kind':'개','weight':'100kg'}

jumsu={'국어' : 90, '수학' : 78, '체육':100}



#[연산자]---------------------------------------------
# 산술 연산 x 
#person+dog

#맴버 연산자 : in, not in
#     key
print('name' in dog)
print('name' in person )

#  value:  dict 타입에서 는 key 만 맴버 연산자로 확인
# print('허스키' in dog)
# print(20 in person)

#value 추출
print( '허스키'in  dog.values())

print( '20'in  person.values())

##[내장함수] --------------------------------------
## - 원소 /요소 개수 확인  :len()---------------------------
print(f' dog 의 요소 개수  : {len(dog)}개')
print(f' person의 요소 개수  : {len(person)}개')

## -원소 요소 정렬 :  sorted()------------------------------
#  -키만 정렬
print( f'dog 오름차순정렬 : {sorted(dog)}')
print( f'dog 내일 차순정렬 : {sorted(dog, reverse=True)}')



jumsu={'국어' : 90, '수학' : 178, '체육':100}
print( f'jumsu 값 오름차순정렬 : {sorted(jumsu.values())}')
print( f'jumsu 키 오름차순정렬 : {sorted(jumsu)}')

print( f'jumsu 값 오름차순정렬 : {sorted(jumsu.items())}')
#print( f'dog 오름차순정렬 : {sorted(dog.values())}')
print( f'jumsu 값 오름차순정렬 : {sorted(jumsu.items(),key = lambda x:x[1])}')

#  -동일한 타입에서 정렬 가능함-------------------------------
n1=[1,4,9,-2]
n2=['a','z','f']
n3=[1,'A',-4,9,'f']
print(sorted(n3))

