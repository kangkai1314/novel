# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_python?city=杭州&cl=false&fromSearch=true&labelWords=&suginput=']

    def parse(self, response):
        print(response)
        po=response.css('title::text').extract_first()
        print (po)

        subs=response.xpath('//ul[@class="item_con_list"]/li[0]')
        print (subs)
        for s in subs:
            print (s)

