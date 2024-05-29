from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')

# downloads the logo from http://pythonscraping.com and stores it as logo.jpg in
# the same directory from which the script is running.
imageLocation = bs.find('a', {'alt': 'python-logo'}).find('img')['src']
urlretrieve (imageLocation, 'logo.jpg')