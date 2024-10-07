#22장 25장p320
a=[10,20,30]
a.append((70,50))
print(a)

a=[10,20,30,70]
a.append(70)
print(a)

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, (1,2))
print(my_list)  # 출력: [1, 2, 'a', 3, 4, 5]

my_list = [1, 2, 3]
result = my_list.reverse()  # my_list가 역순으로 변경되고, result에는 None이 할당됨
print(result)  # 출력: None

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # 출력: [5, 4, 3, 2, 1]


my_list = [4, 2, 1, 3, 5]
my_list.sort()
print(my_list)  # 출력: [1, 2, 3, 4, 5]

my_list = [4, 2, 1, 3, 5]
m=my_list.sort()
print(m)  # 출력: [1, 2, 3, 4, 5]





a = [1, 2, 3]
copied_list = a.copy()
print(a)  # 출력: [1, 2, 3]
print(copied_list)    # 출력: [1, 2, 3]





a.append(4)
print(a)  # 출력: [1, 2, 3, 4]
print(copied_list)  




a=[ i*j  for j in range(1,10) for i in range(2,10)]
    
print(a)

#p270----------------------------------------------------
a=['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']

b=[i for i in a if len(i)==5]
    
    
print(b)

maria ={ 'korean': 94, 'english':91, 'mathematics':89,'science':83}

# 딕셔너리의 값들을 리스트로 가져오기
scores = maria.values()

# 평균 계산
average = sum(scores) / len(scores)

print(f"평균 점수: {average}")

