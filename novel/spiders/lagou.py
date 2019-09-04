# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_python?city=杭州&cl=false&fromSearch=true&labelWords=&suginput=']

    def parse(self, response):
        print(response)
        with open('a.html','w') as f:
            f.write(response.body)
        x=''
        po=response.css('title::text').extract_first()
        print (po)
        b=response.xpath('//li[@class="con_list_item first_row default_list"]')
        print (b)





