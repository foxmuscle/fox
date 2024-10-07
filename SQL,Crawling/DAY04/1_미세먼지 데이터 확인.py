
import pandas as pd
from tabulate import tabulate

# dust.xlsx 불러오기
dust=pd.read_excel('dust.xlsx')


# 데이터 읽어 오기
print(dust.head())
print(tabulate(dust.head(),	headers='keys', tablefmt='pretty'))


# 데이터 확인
print(dust.info())


# 미세 먼지 데이터 가공 : 컬럼 이름 변경
#-한글 컬럼명을 영문으로 변경
dust.rename(columns={'날짜': 'date','아황산가스':'so2','일산화탄소':'co',
                     '오존':'o3','이산화질소':'no2'},inplace=True)

print(tabulate(dust.head(),	headers='keys',	tablefmt='psql'))

# 미세먼지 데이터 가공: 날짜 데이터  변경
#-날짜 데이터 변경 
# -- 기존 데이터:'년도-월-일 시간' -> 변경 : '년도-월-일' 만 추출
dust['date'] = dust['date'].str[:10]
print(tabulate(dust.head(),	headers='keys',	tablefmt='psql'))


#미세먼지 데이터 가공 : 날짜 자료형 변경
dust['date']	=	pd.to_datetime(dust['date'])
print(dust.dtypes)

#미세먼지 데이터 가공 : 컬럼 순서변경

#-['data'] 컬럼에서 년도 , 월, 일 을 추출하여 새로운 컬럼 생성
dust['year']	=	dust['date'].dt.year
dust['month']	=	dust['date'].dt.month
dust['day']	=	dust['date'].dt.day
print(dust.columns)

#- 컬럼 순서 재정렬
dust	=	dust[['date',	'year',	'month',	'day',	'so2',	'co',	'o3',	'no2',	'PM10',	'PM2.5']]
print(dust.columns)

#미세먼지 데이터 전처리 : 누락값(결측치)확인
#-결측치 개수 확인
print('결측치 개수 확인하기')
print(dust.isna().sum())	#	isnull()	동일


#-데이터에서 결측치를 포함하는 행 출력하기
print('결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])


# 미세먼지 데이터 전처리   : 결측치 채우기
print('결측치 채우기')
#dust	=	dust.fillna(method='ffill')	#	Pandas	2.2.0	이전 버전
dust.ffill(inplace=True)	#	Pandas	2.2.0	이후
print(dust.isnull().sum())

#-이전 결측치의 INDEX 를 다시 출력확인
print(dust.iloc[132:134]) #	이전 결측치 index


#날씨 데이터 읽기 및 확인

weather	=	pd.read_excel('weather.xlsx')
print(tabulate(weather.head(),	headers='keys',	tablefmt='psql'))

#출력
print(weather.info())

#날씨 데이터 가공:컬럼 삭제 및 컬럼 이름 변경
#-  불필요한 컬럼(‘지점’, ‘지점명’) 삭제 및 컬럼 이름을 영문으로 변경
weather.drop(['지점',	'지점명'],	axis=1,	inplace=True)
weather.columns =	['date',	'temp',	'wind',	'rain',	'humidity']
print(tabulate(weather.head(),	headers='keys',	tablefmt='pretty'))


#날씨데이터 가공 :시간 정보 삭제
# weather[‘date’] 컬럼에서 시간 정보 삭제 후 데이터 타입 확인
# 기존: 년도-월-일 시간 -> 변경: 년도-월-일

weather['date']	=	pd.to_datetime(weather['date'].dt.date)
print(weather.info())
print(weather.head())

#날씨 데이터 전처리 :결측치 확인
#_ 날씨 데이터 결측치 개수 확인

print('날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())

print('날씨 데이터에서 결측치를 포함하는행 출력')
print(weather[weather.isna().any(axis=1)])

#날씨 데이터 전처리 : 결측치 채우기
# --결측치가 나타 나기 이전의 값으로 채움
weather.ffill(inplace=True)
print(weather.isna().sum())

# 이전 결측치의 index의 값 비교

print(weather.iloc[[368,	565,	742]])

#강수량 데이터 변경

#- 강수량 측정
#기상청에서는 0.1 단위로 강수량을 측정:	강수량이 0.1 이하면 0으로 표시함
#강수량([‘rain’]	컬럼)에서 0인 데이터를 0.01로 변경 후 빈도수 출력
print('강수량이 0인 항목을 0.01로 변경')
weather['rain']	=	weather['rain'].replace(0,	0.01)
print(weather['rain'].value_counts())

# 두 데이터의 크기 확인
#두 데이터를 병합하기 위해 필요 없는 행을 삭제
#미세먼저 데이터와 날씨 데이터의 (행, 열)의 크기 확인

print('dust,	weather의 크기 확인')
print('dust.shape',	dust.shape)
print('weather.shape',	weather.shape)

#미세먼지 데이터에서 공통 내용이 아닌 행 삭제
#미세먼지 데이터의 마지막 부분 확인
print(dust.iloc[740:])

# 날씨 데이터의 마지막 부분 확인
print(dust.iloc[740:])

# 미세먼지 데이터의 마지막 행 삭제 후 크기 확인
dust.drop(index=743,	inplace=True)
print(dust.shape)

#데이터프레임 병합하기 :merge()

# pd.merge(left,right,how='inner',on=None,left_on=None,
#          right_on=None,left_index=True,	right_index=True)

# left데이터프레임.merge(right,how='inner',on= None,left_on=None,
#                  right_on=None,left_index=True,	right_index=True)

# 미세먼지 데이터와 날씨 데이터 병합

print('dust,	weather	데이터프레임 merge')
merged_df =	pd.merge(dust,	weather,	on='date')
print(merged_df.head())

#데이터 분석: 모든 요소별 상관관계 확인


pd.set_option('display.max_columns',	None) # 전체 컬럼 출력
pd.set_option('display.max_rows',	None) # 전체 행 출력
print(merged_df.corr())

#데이터 분석: 메세먼지(PM10)과 상관 관계
#--미세먼지(PM10)를 기준으로 상관관계 분석/ PM10	데이터와 상관관계를 내림차순 정렬
print('미세먼지(PM10)과 상관관계 분석')
corr =	merged_df.corr()
print(corr['PM10'].sort_values(ascending=False))	#	내림차순 정렬


#데이터 시각화 : 히스토그램
import	matplotlib.pyplot as	plt
merged_df.hist(column=['so2','co','o3','no2','PM10','PM2.5','temp','wind','rain','humidity'],
               bins=50,	figsize=(20,15))
plt.show()

#데이터 시각화: 막대 그래프

import	matplotlib.pyplot as	plt
import	seaborn	as	sns
import	koreanize_matplotlib
plt.figure(figsize=(15,	10))
daygraph =	sns.barplot(x='day',	y='PM10',	data=merged_df)
plt.title("날짜별 PM10	농도")
plt.show()

#데이터 시각화: 히트맵 작성
plt.figure(figsize=(15,	10))
sns.heatmap(data=corr,	annot=True,	fmt='.2f',	cmap='hot')
plt.show()

#데이터 시각화: 산점도(PM10과 PM2.5)

plt.figure(figsize=(15,	10))
x	=	merged_df['PM10']
y	=	merged_df['PM2.5']
plt.plot(x,	y,	marker='o',	linestyle='none',	color='red',	alpha=0.5)
plt.title('PM10	vs.	PM2.5')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.show()
