
'''1. 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
- 출근 시간대: 07:00~08:59
-사용 파일: subwaytime.csv	또는 subway.xls
- 07:00~07:59 하차: index[11],	08:00~08:59 하차: index	[13]
- 각 지하철 노선별 가장 많이 내리는 지하철 역 분석
- 1 호선, 2 호선, 3 호선, 4 호선, 5 호선, 6 호선, 7 호선
- 하차 인원은 1,000 단위로 콤마를 찍어서 구분할 것
- 7 개의 지하철 역을 막대 그래프로 표시
- Bar	chart 의 x 축은 (노선 +	지하철 역 이름)을 표시하고, y 축은 인원수를 표시
'''
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


file= 'subwaytime.csv' 

with open(file, 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)  
    next(data)  
    station_list = []
    max_num = -1
    max_station = ''
    
    max_ridership = {}
    lines = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']

    for line in lines:
        tation_list = []
        max_num = -1
        max_station = ''
        for row in data:
            if row[1] == line:
                row[4:] = map(int, row[4:])
                passenger_num = row[11] + row[13]  
                station_name = row[3] + '(' + row[1] + ')'
                if passenger_num > max_num:
                    max_num = passenger_num
                    max_station = station_name
        max_ridership[line] = (max_station, max_num)
        f.seek(0)  
        next(data)  
        next(data)  

#  출력
for line, (station, count) in max_ridership.items():
    print(f"출근 시간대 {line} 최대 하차역: {station}, 하차인원: {count:,}명")

# 그래프 그리기
station_name, station_passenger = zip(*[(f"{line} {station}", count) for line, (station, count) in max_ridership.items()])

plt.figure(figsize=(12, 8))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역', size=16)
plt.bar(station_name, station_passenger)
plt.xticks(rotation=70, fontsize=10)
plt.xlabel('노선 + 지하철 역 이름')
plt.ylabel('하차 인원수')
plt.tight_layout()
plt.show()