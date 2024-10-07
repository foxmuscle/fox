from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import time
import platform
import numpy as np
from PIL import Image


import	collections
if	not	hasattr(collections,	'Callable'):
    collections.Callable =	collections.abc.Callable
#---------------------------------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def url_open():
    url = "https://finance.naver.com/sise/sise_group_detail.naver?type=theme&no=99"
    html = requests.get(url)

    return html

def make_enterprise_list(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    body = soup.find('tbody')
    result = body.find_all('div', {'class' : 'name_area'})

    enterprise_list = []

    for index, enterprise in enumerate(result, start=1):
        # 인덱스 번호를 포함하여 리스트에 추가
        enterprise_list.append((index, enterprise.text.replace("*", "").strip()))

    return enterprise_list

def print_enterprise_table(enterprise_list):
    print("{:<5} {:<20}".format("No", "Enterprise"))
    print("-" * 30)
    for index, enterprise in enterprise_list:
        print("{:<5} {:<20}".format(index, enterprise))

def main():
    html = url_open()
    enterprise_list = make_enterprise_list(html)
    print_enterprise_table(enterprise_list)

main()