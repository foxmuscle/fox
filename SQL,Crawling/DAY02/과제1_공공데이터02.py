import pandas as pd
import matplotlib.pyplot as plt

# 데이터를 읽어들임
file_path = '/mnt/data/subwaytime.csv'  # 실제 파일 경로에 맞게 수정 필요
data = pd.read_csv(file_path)

# 출근 시간대 07:00~08:59 하차 인원 추출
morning_7_to_8 = data.iloc[:, 11]
morning_8_to_9 = data.iloc[:, 13]

# 시간대 합계 계산
morning_total = morning_7_to_8 + morning_8_to_9

# 필요한 노선 목록
subway_lines = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']

# 최대 하차 역 및 인원수 계산
max_stations = {}
for line in subway_lines:
    line_data = data[data['호선'] == line]
    line_morning_total = line_data.iloc[:, 11] + line_data.iloc[:, 13]
    max_station_idx = line_morning_total.idxmax()
    max_station = line_data.loc[max_station_idx, '역명']
    max_count = line_morning_total[max_station_idx]
    max_stations[line] = (max_station, max_count)

# 결과 출력 및 그래프 그리기
stations = []
counts = []
for line, (station, count) in max_stations.items():
    stations.append(f"{line} {station}")
    counts.append(count)

# 1,000 단위 콤마 구분
formatted_counts = [f"{count:,}" for count in counts]

# 결과 출력
for line, (station, count), formatted_count in zip(subway_lines, max_stations.values(), formatted_counts):
    print(f"출근 시간대 {line} 최대 하차역: {station}, 하차인원: {formatted_count}명")

# 막대 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(stations, counts)
plt.xlabel('노선 + 지하철 역 이름')
plt.ylabel('하차 인원수')
plt.title('지하철 각 노선별 최대 하차 인원')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

