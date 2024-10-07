import	csv
f	=	open("daegu.csv",	'r',encoding='utf-8')
data	=	csv.reader(f,	delimiter=',')
count=0
for	row	in	data:
    if	count	>	5:
        break
    else:
        print(row)
    count	+=	1
f.close()

import csv
#	encoding='utf-8-sig'로 '\ufeff'	제거
fin	=	open('daegu.csv',	'r', encoding='utf-8-sig')
data	=	csv.reader(fin,	delimiter=',')

#	newline='':	한 라인씩 건너 뛰며 저장되는 현상 없앰
fout =	open('daegu-utf8.csv',	'w',	newline='',encoding='utf-8-sig')
wr =	csv.writer(fout)

for	row	in	data:
    for	i in	range(len(row)):
        row[i]	=	row[i].replace('\t',	'')
    print(row)			
    wr.writerow(row)	#	writerow(row):	한 행씩 파일로 저장


fin.close()
fout.close()
print('파일 저장 완료')