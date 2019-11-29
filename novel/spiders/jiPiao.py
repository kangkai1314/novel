# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JipiaoSpider(CrawlSpider):
    name = 'jiPiao'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://flights.ctrip.com/itinerary/oneway/hgh-sia?date=2020-01-18']

    rules = (
        Rule(LinkExtractor(allow=r'itinerary/oneway/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        i = scrapy.Item()
        i['title']=response.css('title::text').extract()
        print(i)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
