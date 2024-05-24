from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""
html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html.parser")

name_list = bs.findAll('span', {'class':'green'})
for name in name_list:
    # print(name)
    print(name.get_text()) #strips all tags from document. 
                           #should always be last thing to do. preserve tag structure of a document as long as possible
"""

html2 = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html2, 'html.parser')

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)

# # gets all rows in tables other than the first header row
# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings: # bs.table.tr or bs.tr works as well
#     print(sibling)

# print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# # use regex to find img src that have "../img/gifts/img1.jpg" format
# images = bs.find_all('img', {'src':re.compile(r'\.\.\/img\/gifts/img.*\.jpg')}) 
# for image in images:
#     print(image['src'])

# lambda expressions  - must take a tag object as an argument and return a boolean
# print(bs.find_all(lambda tag: len(tag.attrs) == 2) )#retrieves all tags that have exactly 2 attributes

# equivalent to -> bs.find_all('',text='Or maybe he\'s only resting?')
# lambda expressions can be combined with regex
print(bs.find_all(lambda tag: tag.get_text() ==  'Or maybe he\'s only resting?')) 