from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from konlpy.tag import Okt
import platform
import numpy as np
from PIL import Image
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import	collections

# 한글 폰트 설정 ->폰트 매니저 모듈
from matplotlib import font_manager as fm
from matplotlib import rc

# 적용할 폰트 파일
font_file=r'C:\Windows\Fonts\batang.ttc'

# 폰트 패밀리
font_name= fm.FontProperties(fname=font_file).get_name()

# 새로운 폰트 패밀리 이름 지정
rc('font', family=font_name) 



#-----3자리 숫자 제거 하고 년수 만 뽑은거 --





import matplotlib.pyplot as plt

# 데이터 설정
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [10, 15, 7, 12, 9]

categories = ['1년','2년','3년','4년','5년','10년','3년~10년']
values = [25, 40, 122, 221, 50,27,30]
#[('4년', 334), ('3년', 122), ('2년', 40), ('5년', 32), ('3~10년', 30), ('10년', 27), 
# ('1년', 25), ('5~10년', 11), ('3~15년', 11), ('2~5년', 9), ('2~10년', 9), ('5~8년', 9), ('8년', 9),
#  ('3~20년', 9), ('1~3년', 7), ('1~4년', 7), ('3~5년', 7), ('3~7년', 6), ('3~6년', 6), ('3~12년', 5), 
# ('1~10년', 5), ('12년', 5), ('5~20년', 5), ('7년', 5), ('5~7년', 4), ('7~10년', 4), ('4~10년', 4), 
# ('15년', 4), ('5~15년', 4), ('2~15년', 4), ('10~20년', 3), ('6년', 3), ('7~15년', 3), ('3~8년', 3), 
# ('2~7년', 3), ('1~5년', 3), ('1~15년', 3), ('20년', 3), ('1~6년', 2), ('2~9년', 2), ('2~4년', 2), ('5~16년', 2), 
# ('2~20년', 2), ('2~6년', 2), ('1~8년', 1), ('4~8년', 1), ('6~15년', 1), ('6~20년', 1), ('1~11년', 1), ('11~20년', 1)]
colors = ['#1E90FF', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500',
              '#FFD700', '#00BFFF', '#00CED1', '#00FA9A', '#32CD32',
              '#ADFF2F', '#9ACD32', '#DAA520', '#FF69B4', '#DDA0DD',
              '#8A2BE2', '#6A5ACD', '#9370DB', '#4682B4', '#B0E57C']


# 바그래프 그리기
plt.figure(figsize=(8, 6))
bars=plt.bar(categories, values, color=['#6A5ACD', '#9370DB', '#4682B4', '#B0E57C','#FF8C00', '#FF7F50', '#FF6347']
             ,label='기업수')

# 그래프 제목과 축 라벨 추가
plt.title('채용시 경력별 기업수(년)',size=20)
plt.xlabel('year')
plt.ylabel('기업수')


# 바 위에 숫자 표기
plt.bar_label(bars, fmt='%.2f')



# 범례

plt.legend()


# 그래프 표시
plt.grid()
plt.show()
