from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider): # ArticleSpider extends CrawlSpider
    name = 'articleSpider'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'/wiki/[^:]*$'), callback='parse_items', follow=True, cb_kwargs={'is_article': True}), 
             Rule(LinkExtractor(allow=r'.*'), callback='parse_items', cb_kwargs={'is_article': False})]
    
    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('h1 span::text').get()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract() # xpath - retrieves text content including text in child tags
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ', '')
            print('title is: {} '.format(title))
            # print('text is: {}'.format(text))
            print('Last updated: {}'.format(lastUpdated))
        else:
            print('This is not an article {}'.format(title))
        
