"""
brew services start mysql
mysql -u root
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now().timestamp())

def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES (%s, %s)', (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)[^:]*$'))

links = getLinks('/wiki/Kevin_Bacon')

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()

"""
indexing to make lookups faster. requires more space for the new index

SELECT * FROM dictionary WHERE definition="A small furry animal that says meow";

CREATE INDEX definition ON dictionary (id, definition(16));

"""