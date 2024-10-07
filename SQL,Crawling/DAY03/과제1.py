'''공공데이터 과제 #3 
1. 대구광역시 전체 및 9개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군, 
            군위군) 남녀 비율을 각각의 파이 차트로 구현하세요. (hw03.py)
- subplots를 이용하여 5x2 형태의 총 10개의 subplot을 파이 차트로 구현
- gender.csv 파일 사'''

'''
실행 결과(화면 출력)
대구광역시 :	(남:1,162,046	여:1,205,137)
대구광역시 중구:	(남:44,349	여:48,310)
대구광역시 동구:	(남:168,160	여:175,088)
대구광역시 서구:	(남:81,083	여:82,276)
대구광역시 남구:	(남:65,312	여:71,581)
대구광역시 북구:	(남:206,403	여:210,039)
대구광역시 수성구:	(남:196,513	여:211,798)
대구광역시 달서구:	(남:256,966	여:267,318)
대구광역시 달성군:	(남:131,520	여:127,760)
대구광역시 군위군:	(남:11,740	여:10,967)'''

import	csv
import	matplotlib.pyplot as	plt
import	platform
import	koreanize_matplotlib


f=open('gender.csv',encoding='euc_kr')
data=csv.reader(f)

city_list =	['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', 
             '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', 
             '대구광역시 달서구', '대구광역시 달성군','대구광역시 군위군']

male_list =	[]
female_list =[]	

for	row	in data:
    for	city in	city_list:
        if city in row[0]:
            male_list.append(int(row[104].replace(',','')))
            female_list.append(int(row[207].replace(',','')))

            print(city)
            print("남자 수", male_list)
            print("여자 수", female_list)

# 결과 출력
for i in range(len(city_list)):
    print(f'{city_list[i]}: (남: {male_list[i]:,} 여: {female_list[i]})')



# 파이 차트
# subplots()으로 그리기

fig, axes = plt.subplots(5,2, figsize=(8, 14))

fig.suptitle("대구광역시 구별 남녀 인구 비율", fontsize=20)

for i in range(10):
    
    axes[i//2][i%2].pie( [male_list[i], female_list[i]], labels=['남성','여성'], 
                   autopct='%.1f%%', startangle=90)
    
    axes[i//2][i%2].set_title(f'{city_list[i]}')

plt.show()



         

