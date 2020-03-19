# -*- coding: utf-8 -*-
import scrapy
from novel.items import TestItem


class ScrapyspiderSpider(scrapy.Spider):
    name = 'scrapySpider'
    allowed_domains = ['muyiy.cn']
    start_urls = ['https://muyiy.cn/question/']

    def parse(self, response):
        for href in response.css('a::attr(href)'):
            print(href)
            if href is not None:
                n=response.urljoin(href.extract())
                yield  scrapy.Request(n,callback=self.parse_content)

    def parse_content(self,response):
        print(response)
        title=response.css('title::text')
        print(title.extract_first().encode('gbk'))






