from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class ArticleSpider3(CrawlSpider): 
    name = 'articlePipelines'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'/wiki/[^:]*$'), callback='parse_items', follow=True)]
    
    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1 span::text').get()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()         
        article['lastUpdated'] = response.css('li#footer-info-lastmod::text').extract_first()
        yield article
    
    """
    For output into csv, json or xml run the following in command line:
    $ scrapy runspider articleItems.py -o articles.csv -t csv
    $ scrapy runspider articleItems.py -o articles.json -t json
    $ scrapy runspider articleItems.py -o articles.xml -t xml  
    """