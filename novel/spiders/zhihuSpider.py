# -*- coding: utf-8 -*-
import scrapy


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com']

    def start_requests(self):
        yield  scrapy.Request(self.start_urls[0],cookies={'__utmv':'51854390.100-1|2=registration_date=20140420=1^3=entry_date=20140420=1'})

    def parse(self, response):
        print(response.body)
        with open('a.html','w') as f:
            f.write(response.body)


