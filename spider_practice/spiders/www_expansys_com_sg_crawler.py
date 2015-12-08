import pdb
from datetime import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from spider_practice.items import SpiderPracticeItem


class WwwExpansysComSgCrawler(CrawlSpider):
    name = 'expansys'
    allowed_domains = ['expansys.com.sg']
    start_urls = [
        'http://www.expansys.com.sg/',
    ]

    rules = (
    
    Rule(LinkExtractor(allow = (r'www.expansys.com.sg/\S+\d+/',(r'www.expansys.com.sg/\S+\d+/?page')),deny = (r'.+/.filter')),callback = 'parse_item',follow = True),
    
    )

    def parse_item(self, response):
      for sel in response.xpath('//div[@id = "product"]'):
        item = SpiderPracticeItem()
        item['title'] = sel.xpath('//div[@id="title"]/h1/text()').extract()
        item['brand'] = sel.xpath('//div[@id="title"]/h1/text()').extract()
        item['instock'] = sel.xpath('//li[@id="stock"]/text()').extract()
        item['price'] = sel.xpath('//p[@id="price"]/strong/span/text()').extract()
        item['image_urls'] = sel.xpath('//div[@id="image"]/a/@href').extract()
        item['currency'] = sel.xpath('//p[@id="price"]/meta/@content').extract()
        item['brand'] = sel.xpath('//div[@id="prod_core"]/ul[@class="product-sku"]/li/a[@itemprop="brand"]/text()').extract()
        item['sku'] = sel.xpath('//div[@id="prod_core"]/ul[@class="product-sku"]/li[1]/span/text()').extract()
        
          
        
        print item
        yield item
        
