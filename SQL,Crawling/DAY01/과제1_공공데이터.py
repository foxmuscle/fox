
import	matplotlib.pyplot as	plt
import koreanize_matplotlib
import pandas as pd
#--------------------------------------------------------------------

# title => 그래프 제목
# x_data =>  x 축 데이터 제목
# y_data => y 축 데이터
# max_temp_list => 최고기온 y축
# min_temp_list => 최저기온 y축 
                  
def draw_two_plots(title, x_data, max_temp_list, min_temp_list):
    plt.figure(figsize=(10, 5))
    #최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시 
    #1번
    plt.plot(x_data, max_temp_list, marker='s', linestyle='-', color='red', label='최고기온')
    #2번
    plt.plot(x_data, min_temp_list, marker='s', linestyle='-', color='blue', label='최저기온')
     
    plt.title(title)
    plt.legend()
    plt.show()


def main():
    
    #데이터 가져오기 
    weather= pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
    
    # input 3개
    start_year = int(input("시작 연도를 입력하세요: "))
    end_year = int(input("마지막 연도를 입력하세요: "))
    month = int(input("기온 변화를 측정할 달을 입력하세요: "))
    
    # 데이터를  (datetime) 날짜형식으로
    weather['날짜'] = pd.to_datetime(weather['날짜'], format='%Y-%m-%d')
    
    # 시작 -마지막 연도 
    years =list(range(start_year, end_year + 1))

    # 최고 기온, 최저 기온 담을 리스트
    max_temp_list = []
    min_temp_list = []

    #평균계산 합시다아
    for year in years:
        monthly_data = weather[(weather['날짜'].dt.year == year) & (weather['날짜'].dt.month == month)]
        max_temp_list.append(round(monthly_data['최고기온(℃)'].mean(), 1))
        min_temp_list.append(round(monthly_data['최저기온(℃)'].mean(), 1))
    

       
    # 결과를 출력합니다.
    print(f'{start_year}년부터 {end_year}년까지 {month}월의 기온 변화')
    print(f'{month}월 최저기온 평균: {min_temp_list}')
    print(f'{month}월 최고기온 평균: {max_temp_list}')
        
    #그래프 만들기
    title = f'{start_year}년부터  {end_year}년까지 {month}월의 기온변화'
    draw_two_plots(title, years, max_temp_list, min_temp_list)

main()





