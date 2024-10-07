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





#-----3자리 숫자 제거 하고 년수 만 뽑은거 --





def url_open(url):
    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)

    return html

def make_enterprise_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup2 = soup.find_all('div', {'class' : 'item_recruit'})
    enterprise_list = []
    
    for enterprise in soup2:
        enterprise_list.append('https://www.saramin.co.kr' + enterprise.find('a', {'class' : 'data_layer'}).attrs['href'])
        
    return enterprise_list

def crawling(url_list, driver):

    info = ""
    for url in url_list:    
        try:
            driver.get(url)    

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            soup2 = soup.find_all('strong')
            for information in soup2:
                info += (information.text)
        except Exception as e:
            continue           
    return info

def info_pos(text, list):
    okt = Okt()

    okt_pos = okt.pos(text)
    print(okt_pos)




    for word, tag in okt_pos:
        
        if word == "신입":
            list.append(word)
            continue


        if tag in ['Number']:  # Number 태그를 가진 단어만 선택
            if (word.isdecimal()) and (len(word) < 3):  # 3자리 이상 숫자는 제외
                continue
            if word.find('년') >= 0:  # '년'이 포함된 경우만 추가
                list.append(word)
    print(len(list))
    return list


def make_wordcloud(list):
    counts = Counter(list)
    tags = counts.most_common(50)

    print(tags)
    
    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        font = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
    
    img_mask = np.array(Image.open('cloud.png'))
    wc = WordCloud(font_path = path, width = 400, height = 400,
                   background_color = 'white', max_font_size = 200,
                   repeat = True, colormap = 'inferno', mask = img_mask)

    cloud = wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize = (10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

def main():
    if	not	hasattr(collections, 'Callable'):
        collections.Callable =	collections.abc.Callable

    info_list = []
    driver = webdriver.Chrome()

    for i in range(1, 2):
        url = f"https://www.saramin.co.kr/zf_user/search?searchType=search&searchword=AI&cat_kewd=108&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={i}&recruitSort=relation&recruitPageCount=50&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=y"
        html = url_open(url)
        enterprise_list = make_enterprise_list(html)
        info_text = crawling(enterprise_list, driver)
        info_list = info_pos(info_text, info_list)
    print(len(info_list))
    make_wordcloud(info_list)

main()