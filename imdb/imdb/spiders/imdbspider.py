# coding:utf-8

from scrapy.spiders import CrawlSpider, Request, Rule
from imdb.items import ImdbItem
from scrapy.linkextractors import LinkExtractor

# CrawlSpider inherits Spider
class ImdbSpider(CrawlSpider):
    # name is the attribute inherited from Spider
    # name defines the name of the spider, must be unique, you can instantiating more than one instance
    # of the same spider
    name = 'imdb'



    # allowed_domains is inherited from Spider
    # a list of strings containing domains that this spider id allowed to crawl
    allowed_domains = ['www.imdb.cn']



    # start_urls=['http://www.example.com'] define the first url to crawl, if no definition,
    # the first page will be the start url



    # a new attribute of CrawlSpider
    # rules is a list for one( or more ) Rule Objects, each Rule defines a certain bahavior for crawling 
    # the site.

    # class Rule(link_extrator,callback=none, cb_kwargs=None, follow=None, process_links=None, process_request=None)
    # link_extractor is a LinkExtractor object which defines how links will be extracted from each crawled page.
    # callback is a callable or a string(in which case a method from the spider with that name will be used)
    # to be called for each link extracted from the specific link_extractor.
    # cb_kwargs a dict containning the keyword arguments to be passed to the callback function
    # follow is a boolean which specifies if links should be followed from each response extracted with this rule
    
    # class LinkExtractor is the same as LxmlLinkExtractor
    # Parameters:
    # allow=(a (or list of) regular expression):the regular expressions the urls must match in order to be extracted,if empty,it will match all
    # deny=(a (or list of )regular expression):the urls must match in order to be excluded, if not given, it won't exclude any links.
    # allow_domains=(str or list):a string or a list string containing domains which will be considered for extracting the links
    # deny_domains=(str or list)
    rules = (
        Rule(LinkExtractor(allow=r"/title/tt\d+$"), callback="parse_imdb", follow=True),
    )



    # start_requests() is inherited from Spider
    def start_requests(self):
        pages = []
        for i in range(1, 14616):
            url = "http://www.imdb.cn/nowplaying/" + str(i)
            yield Request(url=url, callback=self.parse)

    def parse_imdb(self, response):
        item = ImdbItem()
        item['url'] = response.url
        item['title'] = "".join(response.xpath('//*[@class="fk-3"]/div[@class="hdd"]/h3/text()').extract())
        pass