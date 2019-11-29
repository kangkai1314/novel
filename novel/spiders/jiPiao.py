# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import JiPiaoItem
from scrapy.loader import ItemLoader


class JipiaoSpider(scrapy.Spider):
    name = 'jiPiao'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://flights.ctrip.com/itinerary/oneway/hgh-sia?date=2020-01-18']

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        with open('xiecheng.html','w') as f:
            f.write(response.body)
        loader=ItemLoader(item=JiPiaoItem(),response=response)
        loader.add_css('title','title::text')
        loader.add_css('price','span::text')
        return loader.load_item()

