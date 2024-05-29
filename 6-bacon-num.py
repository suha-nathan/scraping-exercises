from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import shuffle
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

"""
inserts a new page record if it doesnt already exist
returns the page id of existing or newly inserted page
"""
def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url=%s', (url))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)',(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]
"""
returns list of all pages in database.
** the return value pages determines whether or not to visit a page.
As soon as each page is loaded, all links on the page are stored as pages, 
even though they have not been visited yet - just that their links have been seen.

if the crawler is restarted, all the pages that are stored in the db that are
"seen but not visited" will not be visited. That page's links will not be recorded.
fix: adda boolean visited variable to each page record.
"""
def loadPages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()]
    return pages

"""
creates a new link record in the database if it doesnt already exist. 
"""
def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId=%s AND toPageId=%s',(int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s,%s)',(int(fromPageId), int(toPageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel, pages):
    print("recursion level: ",recursionLevel)
    # if recursionLevel > 4: 
    if recursionLevel > 2: 
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)[^:]*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        insertLink(pageId, insertPageIfNotExists(link))
        if link not in pages:
            pages.append(link)
            getLinks(link, recursionLevel+1, pages)

getLinks('/wiki/Kevin_Bacon', 0, loadPages())

cur.close()
conn.close()