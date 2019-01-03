"""
    Using the requests and BeautifulSoup Python libraries,
    print to the screen the full text of the article on this website:
    http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
"""
import requests
from bs4 import BeautifulSoup

url = 'http://coreyms.com'
r = requests.get(url).text

soup = BeautifulSoup(r, features="html5lib")

data = soup.find('div', class_='boxframe center')

title = data.h2.text

sumary = data.p.text

print title
print sumary
