from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import requests
import collections
import pandas as pd
from tabulate import tabulate

# Callable 에러 해결
# AttributeError: module 'collections' has no attribute 'Callable'
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable


url='''
<div class="row rowReceipt" id="rowGuidelines">
    <h2 class="header">모집요강</h2>
        <div class="field">
            <div class="label">경력</div>
            <div class="value">
                <span class="point-color">경력무관</span>
<br />
            </div>
        </div>
            <div class="field">
            <div class="label">학력</div>
            <div class="value">
                <span class="point-color">대졸이상</span>

            </div>
        </div>
            <div class="field">
            <div class="label">고용형태</div>
                <div class="value">
                    <span class="point-color">정규직</span>

                        <span class="sub-text">
                            

                        </span>
                </div>
        </div>

        <div class="field">
            <div class="label">
                급여
                    <span class="salary-type">연봉</span>
            </div>
            <div class="value">
                4,000~10,000만원

                    <span class="point-color">면접 후 결정</span>


            </div>
        </div>

    <div class="field">
        <div class="label">근무지역</div>
        <div class="value">
            충남 천안시 서북구
        </div>
    </div>

        <div class="field">
            <div class="label">직급/직책</div>
            <div class="value">
팀원, 팀장/매니저/실장, 파트장/그룹장
            </div>
        </div>
            <div class="field">
            <div class="label">근무시간</div>
            <div class="value">
                주5일(월~금)
 08:30~17:30, 재택근무 가능, 탄력근무제            </div>
        </div>
            <div class="field">
            <div class="label">우대조건</div>
            <div class="value">
석사학위 수여자, 박사학위 수여자, 유관업무 경력자                                                                            </div>
        </div>

        <div class="field">
            <div class="label">스킬</div>
            <div class="value">
                OpenCV, VIsualC·C++, AI
            </div>
        </div>

        <div class="field">
            <div class="label">핵심역량</div>
            <div class="value">
                        <strong>성취지향성, </strong>

                창의성, 협동심, 계획성, 성실성
            </div>
        </div>

        <div class="field">
            <div class="label">모집인원</div>
            <div class="value">
                ○명
            </div>
        </div>
</div>
'''

soup = BeautifulSoup(url, 'html.parser')
# 모집요강 섹션을 찾기
guidelines_section = soup.find('div', {'id': 'rowGuidelines'})

# 모집요강 정보 저장할 딕셔너리 초기화
job_info = {}

# 모든 'field' 클래스 요소를 찾기
fields = guidelines_section.find_all('div', class_='field')

# 각 field에서 라벨과 값을 추출하여 딕셔너리에 저장
for field in fields:
    label = field.find('div', class_='label').get_text(strip=True)
    value = field.find('div', class_='value').get_text(strip=True)
    job_info[label] = value


# 연봉 정보가 있는지 확인하여 처리
    if "급여" in label:
        salary_type = field.find('span', class_='salary-type').get_text(strip=True)
        value = f"{salary_type} {value}"
    
    job_info[label] = value




# 데이터프레임으로 변환
df = pd.DataFrame(list(job_info.items()), columns=['항목', '내용'])

# 표 형태로 출력
print(tabulate(df, headers='keys', tablefmt='pretty'))


#---------------------------------------------------------------------------
# html=requests.get(url)
# soup = BeautifulSoup(url, 'html.parser')
# # print(soup.select_one('div#title').string)
# soup2 = soup.find_all('div')
# # print(soup2)
# L = []
# for msg in soup2:
#     L.append(msg.text.replace("\n", "").strip())

# print(L)
#--------------------------------------------------------------------------
