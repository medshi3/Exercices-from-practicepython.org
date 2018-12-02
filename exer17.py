"""
    Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text, features="html5lib")
title = soup.find_all('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print ttl_lst
