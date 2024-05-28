from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

"""
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html,'html.parser')
    for link in bs.find('div',{'id':'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
"""
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0]) #first paragraph in a wiki article page
        print(bs.find(id='ca-edit').find('a').attrs['href'])  #edit button/link
    except AttributeError:
        print('This page is missing something! Continuing.')
    except IndexError:
        print("No paragraphs found in content! Continuing")
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('/wiki/Michael_Bacon_(musician)')