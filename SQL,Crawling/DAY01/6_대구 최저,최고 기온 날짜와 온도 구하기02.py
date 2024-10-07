import csv
import numpy as np
def get_min_max_numpy(data):
    next(data)

    max_temp_list = list()
    min_temp_list = list()
    data_list =list()

    for row in data :
        if row[3] == '':
            row[3] =100
        if row[4] =='':
            row[4] = -999

        min_temp_list.append(row[3])
        max_temp_list.append(row[4])	
        data_list.append(row[0])

    max_temp_array =	np.array(max_temp_list)	 #	리스트를 ndarray로 변경
    max_temp_array =	max_temp_array.astype(float) #	문자열 형태를 float으로 변경
    max_temp =	max_temp_array.max()	 #	최대값 리턴
    max_index =	max_temp_array.argmax()	 

    min_temp_array =	np.array(min_temp_list)	 #	리스트를 ndarray로 변경
    min_temp_array =	min_temp_array.astype(float)
    min_temp =	min_temp_array.min()	 #	최소값 리턴
    min_index =	min_temp_array.argmin()	

    print(f'대구 최저 기온 날짜:	{data_list[min_index]},	온도:	{min_temp}')
    print(f'대구 최고 기온 날짜:	{data_list[max_index]},	온도:	{max_temp}')


def	main():
    f	=	open('daegu-utf8.csv',	'r',	encoding='utf-8-sig')
    data	=	csv.reader(f)
    get_min_max_numpy(data)
    f.close()
main()