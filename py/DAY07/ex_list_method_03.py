#------------------------------------------------------
# 리스트 전용의 함수, 즉 메서드 (methed)
# -리스트의 원소/ 요소 를 제어 하기 위한 함수
#------------------------------------------------------

# [메서드- 요소 순서 제어 메서드 reverse()]----------------

import random as rad

rad.seed(3) # 동일한 랜덤 숫자 추출을 위한 기준점

datas=[]
for _ in range(10) :
    datas.append(rad.randint(1,30))

print(f' {len(datas)}개 , {datas}')

# 제일 앞 0--> -1번으로  ,-1번을 0번으로 위치를 변경------------


datas.reverse()
print(f' {len(datas)}개 , {datas}')




# [메서드- 요소의 크기를 비교해서 장렬해주는  메서드 sort()]----------------
## -기본정렬 : 오름차순 즉, 작은 데이터부터 큰 데이터 순서
datas.sort()
print(f' {len(datas)}개 , {datas}')


## -기본정렬 : 내림차순 즉, 큰데이터에서 작은데이터 순서------------------
datas.sort(reverse=True)
print(f' {len(datas)}개 , {datas}')





# [메서드- 리스트에서 요소를 꺼내는 메서드 pop()]----------------
## -리스트에서 요소가 삭제됨
value=datas.pop()        # 제일 마지막 원소/ 요소
print(f'avlue : {value}-{len(datas)}개 , {datas}')

value=datas.pop(0)        # 특정 인덱스의 원소/ 요소 꺼내기
print(f'avlue : {value}-{len(datas)}개 , {datas}')

# [메서드- 리스트 확장시켜주는 메서드 extend()]----------------

datas.extend([11,22,33])
print(f'{len(datas)}개 , {datas}')


datas.extend((555,777))
print(f'{len(datas)}개 , {datas}')


datas.extend(('good luck'))
print(f'{len(datas)}개 , {datas}')

datas.extend({555,777,555,777})
print(f'{len(datas)}개 , {datas}')


datas.extend({'name' : '홍길동','age': 12})
print(f'{len(datas)}개 , {datas}')


# [메서드- 모든 원소 삭제 메서드 clear()]----------------
datas.clear()
print(f'{len(datas)}개 , {datas}')