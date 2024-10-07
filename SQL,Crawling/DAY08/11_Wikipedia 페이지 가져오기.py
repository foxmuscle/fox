#  Kevin	Bacon 위키피디아 URL
# • https://en.wikipedia.org/wiki/Kevin_Bacon


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(
)
bs = BesutifulSoup(html, 'html.parser')
body_content = bs.find('div', {'id':'bodyContent'})

pattern = 
for link in body_content.