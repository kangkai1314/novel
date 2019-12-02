# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import JiPiaoItem
from scrapy.loader import ItemLoader
from novel.util import writeResponse


class JipiaoSpider(scrapy.Spider):
    name = 'jiPiao'
    allowed_domains = ['ctrip.com']
    #start_urls = ['https://flights.ctrip.com/itinerary/oneway/hgh-sia?date=2020-01-18']
    start_urls=['https://sjipiao.fliggy.com/flight_search_result.htm?_input_charset=utf-8&spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%E6%9D%AD%E5%B7%9E&depCity=&depDate=2020-01-19&arrCityName=%E8%A5%BF%E5%AE%89&arrCity=SIA&arrDate=&ttid=seo.000000574']

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        writeResponse(self,response)
        loader=ItemLoader(item=JiPiaoItem(),response=response)
        loader.add_css('title','title::text')
        loader.add_css('price','span::text')
        return loader.load_item()

