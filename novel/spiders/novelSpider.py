# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from novel.items import NovelItem

class NovelspiderSpider(scrapy.Spider):
    name = 'novelSpider'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com']

    def parse(self, response):
        books=response.xpath('//*[@id="container"]/section/ul')
        for book in books:
            print book
            name=book.xpath('/section/ul/li/a')














