from datetime import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from spider_practice.items import SpiderPracticeItem


class WwwExpansysComSgCrawler(CrawlSpider):
    name = 'allforyou'
    allowed_domains = ['allforyou.sg']
    start_urls = [
        'https://allforyou.sg/',
    ]

    rules = (
    
    Rule(LinkExtractor(allow = (r'allforyou.sg/',r'allforyou.sg/.+pagenumber=\d')),callback = 'parse_dir_contents',follow = True),
    
    )
    listSku=[]
    def parse_dir_contents(self, response):
      for sel in response.xpath('//div[@class="prod-data"]'):
        item = SpiderPracticeItem()
        if sel.xpath('@data-newprodid').extract() not in self.listSku:
          self.listSku.append(sel.xpath('@data-newprodid').extract())
          item['title'] = sel.xpath('@data-name').extract()
          item['price'] = sel.xpath('@data-price').extract()
          item['instock'] = sel.xpath('@data-outofstock').extract()
          item['image_urls'] = sel.xpath('@data-imgurl').extract()
          item['sku'] = sel.xpath('@data-newprodid').extract()
          yield item
          

      