students=[('Alice',	3.9,	20160303),
          ('Bob',	3.0,	20160302),
          ('Charlie',	4.3,	20160301)]

#	학번(students[2])을 기준으로 오름차순 정렬
sorted_students1	=	sorted(students,	key	=	lambda	s:	s[2])
print(sorted_students1)
#	학점(students[1])을 기준으로 내림 차순 정렬
sorted_students2	=	sorted(students,	key	=	lambda	s:	s[1],	reverse=True)
print(sorted_students2)

class	Student:
    def	__init__(self,	name,	grade,	number):
        self.name =	name
        self.grade =	grade
        self.number =	number
    def	__repr__(self):
        return	f'({self.name},	{self.grade},	{self.number})'
#	Student	객체 리스트 생성
students	=[Student('홍길동',3.9,20240303), Student('김유신',3.0,20240320),Student('박문수',4.3,20240301)]

print(students[0])
print('-'*50)
print('Student객체의 name을 기준으로 정렬')
sorted_list =	sorted(students,	key=lambda	s:	s.name)
print(sorted_list)