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

    for enterprise in result:
        enterprise_list.append(enterprise.text.replace("*", "").strip())

    return enterprise_list
def main():
    html = url_open()
    L = make_enterprise_list(html)
    print(L)

main()


