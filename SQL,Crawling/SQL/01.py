import pymysql
import pandas as pd
import csv

conn=pymysql.connect(host='localhost',	user='root',	password='1234',
db='sakila',	charset='utf8')

cur	=	conn.cursor()
cur.execute('select	*	from	language')

desc	=	cur.description #	헤더 정보를 가져옴
for	i in	range(len(desc)):
    print(desc[i][0],	end='	')
print()

rows	=	cur.fetchall()	#	모든 데이터를 가져옴
for	data	in	rows:
    print(data)
print()

cur.close()
conn.close()	#	데이터베이스 연결 종료












#  pymysql.connect() 함수
#  host:	DB가 존재하는 서버의 주소(localhost 또는 IP주소)
# user:	사용자 ID,	db:	연결할 데이터베이스 이름
# 리턴: Connection 객체



import	pymysql
import	pandas	as	pd

conn	=	pymysql.connect(host='localhost',	user='root',password='1234',
                       db ='sakila',	charset='utf8')
cur =	conn.cursor()
cur.execute('select	* from language')
rows	=	cur.fetchall()	#	모든 데이터를 가져옴
print(rows)

language_df =	pd.DataFrame(rows)	
print(language_df)

cur.close()
conn.close()	#	데이터베이스 연결 종료



#  DictCursor 사용
#  pymysql.connect(,	cursorclass=pymysql.cursors.DictCursor)
#  conn.cursor(pymysql.cursors.DictCursor)
#  DataFrame의 column들을 같이 리턴함

import	pymysql
import	pandas	as	pd
conn	=	pymysql.connect(host='localhost',	user='root',	password='1234',
db='sakila',	charset='utf8')
cur	=	conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select	*	from	language')
rows	=	cur.fetchall()	#	모든 데이터를 가져옴
language_df =	pd.DataFrame(rows)	#	DataFrame 형태로 변환
print(language_df)
#print(language_df.iloc[0:3])
print()
print(language_df['name'])
cur.close()
conn.close()	#	데이터베이스 연결 종료


#  복잡한 쿼리 실행
# § inner	join 내용

import pymysql

conn = pymysql.connect(host = 'localhost', user= 'root',password ='1234', db ='sakila',charset = 'utf8')

cur = conn.cursor()

query = """
select	c.email
from	customer	as	c
inner	join	rental	as	r
on	c.customer_id =	r.customer_id
where	date(r.rental_date)	=	(%s)"""

cur.execute(query,	('2005-06-14'))
rows	=	cur.fetchall()	#	모든 데이터를 가져옴
for	row	in	rows:
    print(row)
cur.close()
conn.close()


# 테이블 생성


import pymysql
def	create_table(conn,	cur):
    try:
        query1	=	"drop	table	if	exists	customer"
        query2	=	"""
            create	table	customer
            (name	varchar(10),	
            category	smallint,	
            region	varchar(10))
            """
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)

def	main():
    conn=	pymysql.connect(host='localhost',	user='root',password='1234', db='sqlclass_db',charset='utf8')
    cur	=conn.cursor()

#	테이블 생성 함수 호출
    create_table(conn,	cur)
#	연결 종료
    cur.close()
    conn.close()
    print('Database	연결 종료')
main()



# execute() 예제
import	pymysql

conn= pymysql.connect(host='localhost',	user='root',	password='1234',
db='sqlclass_db',	charset='utf8')

curs	=	conn.cursor()
sql =	"""insert	into	customer(name,	category,	region)
values	(%s,	%s,	%s)"""

curs.execute(sql,	('홍길동',	1,	'서울'))
curs.execute(sql,	('이연수',	2,	'서울'))
conn.commit()

print('INSERT	완료')

curs.execute('select	*	from	customer')
rows	=	curs.fetchall()	#	모든 데이터를 가져옴
print(rows)

curs.close()
conn.close()