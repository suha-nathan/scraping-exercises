from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

"""
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), "html.parser")

#use regex to get all article links
for link in bs.find('div',{'id':'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
"""
random.seed(datetime.datetime.now().timestamp())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html,'html.parser')
    return bs.find('div',{'id':'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)


