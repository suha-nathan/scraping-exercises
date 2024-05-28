import requests
from bs4 import BeautifulSoup

class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body
    
    def print(self):
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl # defines where you should go to get search results if you append the topic you are looking for
        self.resultListing = resultListing # defines the html/css box that holds information about each result
        self.resultUrl = resultUrl # defines the tag inside the box that gives the exactURL for the result
        self.absoluteUrl = absoluteUrl # boolean - if search results are absolute or relative
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    
    def safeGet(self, pageObj, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty
        string if no object is found for the given selector
        """
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ""
    
    def search(self, topic, site):
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
            #check if absolute or relative url
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)

            if bs is None:
                print("Something was wrong with that page or URL. Skipping!")
                return
            
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()
            
    
    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            print("trying to print title: ", title)
            print("trying to print body: ", body)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

'''
crawler = Crawler()
siteData = [['O\'Reilly Media', 'http://oreilly.com','h1', 'section#product-description'],['Reuters', 'http://reuters.com', 'h1','div.StandardArticleBody_body_1gnLA'],['Brookings', 'http://www.brookings.edu','h1', 'div.post-body'],['New York Times', 'http://nytimes.com','h1', 'p.story-content']]
websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

print("starting")
crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')
'''

crawler = Crawler()
siteData = [['O\'Reilly Media', 'http://oreilly.com','https://ssearch.oreilly.com/?q=','article.product-result','p.title a', True, 'h1', 'section#product-description'],
['Reuters', 'http://reuters.com','http://www.reuters.com/search/news?blob=','div.search-result-content','h3.search-result-title a',False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu','https://www.brookings.edu/search/?s=','div.list-content article', 'h4.title a', True, 'h1','div.post-body']]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    
topics = ['python', 'data science']
for topic in topics: #pay attention to the way the loops are structured to distribute requests to a site over a period of time
    print("GETTING INFO ABOUT: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)

