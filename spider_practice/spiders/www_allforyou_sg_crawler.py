from datetime import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from spider_practice.items import SpiderPracticeItem


class WwwExpansysComSgCrawler(CrawlSpider):
    name = 'allforyou'
    allowed_domains = ['allforyou.sg']
    start_urls = [
        'http://www.allforyou.sg/',
    ]

    def parse(self, response):
      for href in response.xpath('//div[@class="treemenu-level2"]/a/@href'):
        url = response.urljoin(href.extract())
        yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
      for sel in response.xpath('//div[@class="prod-data"]'):
        item = SpiderPracticeItem()
        item['title'] = sel.xpath('@data-name').extract()
        item['price'] = sel.xpath('@data-price').extract()
        item['instock'] = sel.xpath('@data-outofstock').extract()
        item['image_urls'] = sel.xpath('@data-imgurl').extract()
        item['sku'] = sel.xpath('@data-newprodid').extract()
        print item
        yield item