import scrapy

class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self): #scrapy defined entry point - generates request objects to crawl the website
        urls = ['http://en.wikipedia.org/wiki/Python_%28programming_language%29','https://en.wikipedia.org/wiki/Functional_programming', 'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):
        url = response.url
        title = response.css('h1 span::text').get()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))

    
