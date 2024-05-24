from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.body.h1)

# HTTP error 404, 500 etc handling
# URL error handling when server is down or doesn't exist
try:
    html = urlopen('https://pythonscrapingURLDOESNTEXIST.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server couldn\'t be found')
else:
    print('It worked!')

# if a tag is not found (return type is None) or accessing another function on a None object (AttributeError)
try:
    badContent = bs.nonExistentTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)

