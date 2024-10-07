
'''아래에 주어진 총 6개 나라의 수도에 대한 국가명, 대륙, 인구수를 표시한 테이블을 이용하여
딕셔너리를 작성하고, 아래 실행 화면과 같이 출력을 하는 프로그램을 작성하시오.'''




#전체
def print_all_data(city_data):
    for i, (city, details) in enumerate(city_data.items(), start=1):
        print(f"[{i}] {city}: {details}")
#오름 차순
def print_sorted_by_city(city_data):
    sorted_cities = sorted(city_data)
    for i, city in enumerate(sorted_cities, start=1):
        country, continent, population = city_data[city]
        print(f"[{i}] {city:<15}: {country:<15} {continent:<10} {population:,}")

while True:
        print("-----------------------------------------")
        print("1. 전체 데이터 출력")
        print("2. 수도 이름 오름차순 출력")
        print("3. 모든 도시의 인구수 내림차순 출력")
        print("4. 특정 도시의 정보 출력")
        print("5. 대륙별 인구수 계산 및 출력")
        print("6. 프로그램 종료")
        print("-----------------------------------------")
        menu = input("메뉴를 입력하세요: ")





print('교수님 .. 넘 힘들어요ㅠ')
     