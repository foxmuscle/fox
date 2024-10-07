import	csv

f= open('seoul.csv','r',encoding='euc-kr')			#	cp949도 동일
data= csv.reader(f,	delimiter=',')
for	row	in	data:
       if	''	in	row:
           print(row)

f.close()